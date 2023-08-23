#!/usr/bin/env python
# coding: utf-8

# In[115]:


import pandas as pd


# In[116]:


data = pd.read_csv('Ecommerce Purchases')


# In[117]:


data.to_string()


# In[118]:


data.columns


# In[119]:


data


# In[120]:


# Display Top 10 Rows Of The DataSet
data.head(10)


# In[121]:


# Check Last 10 Rows Of The DataSet
data.tail(10)


# In[122]:


# Check DataType Of Each Column
data.dtypes


# In[123]:


# Check Null Values In The DataSet
data.isnull()


# In[124]:


data.isnull().sum()


# In[125]:


# How Many Rows And Columns In Our DataSet\
print("Total Number Of Columns Are:",len(data.columns))


# In[126]:


data.columns


# In[127]:


print("Total Number Of Rows Are:", len(data))


# In[128]:


data.info()


# In[129]:


# For Highest and Lowest Purchase Price

data['Purchase Price'].max() #For Highest Purchase Price


# In[130]:


data['Purchase Price'].min() #For Lowest Purchase Price


# In[131]:


# Find Average Purchase Price

data['Purchase Price'].mean()


# In[132]:


# How Many People Have French 'fr' As Theor Language

data['Language']


# In[133]:


data['Language']=='fr'


# In[134]:


len(data[data['Language']=='fr'])


# In[135]:


data[data['Language']=='fr'].count()


# In[136]:


#Find Job Titles Contain Engineers

data.columns


# In[137]:


data['Job']=='Engineers'


# In[138]:


len(data['Job']=='Engineers')


# In[139]:


data[data['Job']=='Engineers'].count()


# In[140]:


len(data[data['Job'].str.contains('engineer',case=False)])


# In[141]:


# Find Email Of The Person With The Following IP Address:
# 132.207.160.22

data.columns


# In[142]:


data['IP Address']=='132.207.160.22'


# In[143]:


len(data['IP Address']=='132.207.160.22')


# In[144]:


data[data['IP Address']=='132.207.160.22'] ['Email']


# In[145]:


# How Many People Have MasterCard As Their Credit Card Provider And Made A Purchase Above 50
data.columns


# In[146]:


data


# In[147]:


len(data[(data['CC Provider'] == 'Mastercard')  & (data['Purchase Price']>50)])


# In[148]:


data[(data['CC Provider'] == 'Mastercard')  \
     & (data['Purchase Price']>50)].count()


# In[149]:


# Find The Email Of The Person With The Following Credit Card Number:
# 4664825258997302

data.columns


# In[150]:


data[data['Credit Card']==4664825258997302] ['Email']


# In[151]:


# How Many People Purchase During The AM And PM

data.columns


# In[152]:


data['AM or PM'].value_counts()


# In[153]:


# How Many People Have A Credit Card That Expires In 2020

def func():
    count=0
    for x in data['CC Exp Date']:
        if x.split('/')[1]=='20':
            count = count+1
    print(count)
func()        


# In[154]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# In[158]:


# Top 5 Most Popular Email Providers (e.g. gmail.com,yahoo.com,etc)
list1 = []
for x in data['Email']:
    list1.append(x.split('@')[1])

data['Temp']=list1

data.head(1)


# In[160]:


data['Temp'].value_counts().head()


# In[168]:


data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()


# In[ ]:




