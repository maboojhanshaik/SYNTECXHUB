#!/usr/bin/env python
# coding: utf-8

# Importing the required packages

# In[14]:


import pandas as pd


# Reading the CSV File

# In[15]:


raw_data=pd.read_csv("bank-additional/bank-additional/bank.csv",sep=';')


# Exploring the data

# In[16]:


raw_data.info()


# In[17]:


raw_data.dtypes


# In[18]:


raw_data.head()


# In[19]:


raw_data.tail()


# In[20]:


raw_data.describe()


# Filtering the data based on age criteria i.e age>=50

# In[21]:


age50=raw_data[raw_data['age']>=50].reset_index(drop=True)
age50.index=age50.index+1
age50.head()


# Filtering the consumers having house loan

# In[22]:


house_loan_status_yes =raw_data[raw_data['housing']=='yes'].reset_index(drop=True)
house_loan_status_yes.index=house_loan_status_yes.index+1
house_loan_status_yes.head()


# Filtering High campaign contacts (>5)

# In[23]:


high_campaign =raw_data[raw_data['campaign']>5].reset_index(drop=True)
high_campaign.index=high_campaign.index+1
high_campaign.head()


# Selecting required colums

# In[24]:


required_colums = raw_data[['age', 'job', 'loan', 'y']].reset_index(drop=True)
required_colums.index=required_colums.index+1
required_colums.head()


# Taking subset of first 100 rows and 300 to 400 rows 

# In[25]:


first_100=raw_data.iloc[:100]
first_100.index=first_100.index+1
first_100


# In[26]:


rows_300_400=raw_data.iloc[300:400]
rows_300_400.index=rows_300_400.index+1
rows_300_400


# Saving the files

# In[27]:


age50.to_csv("customers_above_50.csv", index=False)


# In[29]:


age50.to_excel("customers_above_50.xlsx", index=False)


# In[ ]:




