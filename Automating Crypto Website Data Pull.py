#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b9b4dc8f-bd05-4569-8e02-cf145bdee333',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[3]:


import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', None)


# In[4]:


df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')


# In[5]:


df


# In[6]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'15',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'b9b4dc8f-bd05-4569-8e02-cf145bdee333',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')
    df

    if not os.path.isfile(r"D:\g\API.csv"):
        df.to_csv(r"D:\g\API.csv", header = 'column_names')
    else:
        df.to_csv(r"D:\g\API.csv",mode = 'a', header = False)


# In[40]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API Runner Completed Successfully')
    sleep(15)
exit()


# In[41]:


pd.set_option('display.float_format', lambda x : '%.5f' %x)


# In[9]:


df.head()


# In[42]:


df3 = df.groupby('name', sort = False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()
df3


# In[43]:


df4 = df3.stack()
df4


# In[44]:


df5 = df4.to_frame(name = 'values')
df5


# In[45]:





# In[13]:


count = df5.count()


# In[45]:


index = pd.Index(range(90))
df6 = df5.set_index(index)
df6


# In[46]:


df6 = df5.reset_index()


# In[47]:


df7 = df6.rename(columns = {'level_1': 'percent_change'})


# In[ ]:





# In[48]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[49]:


sns.catplot(x = 'percent_change',y = 'values', hue = 'name',data = df7, kind = 'point',aspect = 3, height = 5)

