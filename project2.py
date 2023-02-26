#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install apyori')


# In[2]:


get_ipython().system('pip install apriori')


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
df


# In[5]:


df.values.tolist()


# In[6]:


t=[]
for i in range(len(df)):
    t.append([str(df.values[i,j]) for j in range(0,20)  if str(df.values[i,j])!='nan'])


# In[7]:


t


# In[8]:


from apyori import apriori


# In[9]:


rules=apriori(t,min_support=0.003,min_confidence=0.35,min_lifts=3,min_length=2)


# In[10]:


list(rules)


# In[11]:


D=df.values.ravel()
D


# In[12]:


import collections
val=collections.Counter(D)
val


# In[13]:


val.items()


# In[14]:


data=pd.DataFrame(val.items())
data


# In[18]:


data=data.rename(columns={0:'items',1:'Total'})
data


# In[20]:


data.sort_values(by='Total',ascending=False)[1:]


# In[ ]:




