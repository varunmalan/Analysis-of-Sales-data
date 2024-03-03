#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


df =pd.read_csv("Diwali Sales Data.csv")


# In[13]:


import pandas as pd

# Specify the encoding when reading the CSV file
df = pd.read_csv("Diwali Sales Data.csv", encoding='ISO-8859-1')


# In[14]:


df.shape


# In[16]:


df.head()


# In[18]:


df.info()


# In[19]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[21]:


df.isnull()


# In[25]:


df.isnull().sum()


# In[26]:


df.dropna(inplace=True)


# In[27]:


df.shape


# In[28]:


df.isnull().sum()


# In[29]:


# change of datatype 
df['Amount'] = df['Amount'].astype('int')


# In[30]:


df['Amount'].dtypes


# In[33]:


df.columns


# In[34]:


#rename column 
df.rename(columns = {'Marital_Status' : 'Shaadi'})


# In[35]:


df.describe()


# In[36]:


# use describe on the partcular column or specific column 
df[['Age', 'Orders', 'Amount']].describe()


# In[37]:


# Exploratory Data Analysis 


# In[38]:


# on the Gender COlumn 


# In[39]:


ax = sns.countplot(x = 'Gender', data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x= 'Gender', y='Amount', data=sales_gen)


# In[45]:


# From the above graph We can see that most of the graph is Female buyers and can come on conclusion that Female Purchased more then the male. 


# In[46]:


# Age 


# In[47]:


df.columns


# In[49]:


ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[50]:


ax = sns.countplot(data=df, x='Age Group')
for bars in ax.containers:
    ax.bar_label(bars)


# In[56]:


# Total AMount Vs Age Group 
Sales_age = df.groupby(['Age Group'], as_index= False)['Amount'].sum().sort_values(by='Amount', ascending = False)
sns.barplot (x='Age Group', y='Amount', data=Sales_age)


# In[57]:


## From Above graph we can see that most of the buyers are in the age of  group of 26-25 and that are Females.


# In[58]:


df.columns


# In[59]:


# By Marital Status 


# In[60]:


ax = sns.countplot(data=df, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)


# In[84]:


ax = sns.countplot(data=df, x='Marital_Status', hue='Gender')
sns.set(rc={'figure.figsize':(15,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


#Check the Sales for the column Maritsal staus Vs Amount
sales_maritalstatus= df.groupby(['Marital_Status'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Marital_Status', y='Amount', data=sales_maritalstatus)


# In[64]:


sales_maritalstatus= df.groupby(['Marital_Status'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Marital_Status', y='Amount', data=sales_maritalstatus)


# In[65]:


# From the above graph it is clear that marital people spent more amount in sales. 


# In[66]:


#By State


# In[70]:


ax = sns.countplot(data=df, x='State', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    sns.set(rc={'figure.figsize':(15,5)})


# In[80]:


sales_States= df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='State', y='Orders', data=sales_States)


# In[81]:


sales_States= df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='State', y='Amount', data=sales_States)


# In[82]:


# Above graph states that Number of Orders and AMount spend is Highest from Uttar pradesh and Follows by Maharashtra. 


# In[85]:


# Occupation 


# In[87]:


sales_Occupation= df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='Occupation', y='Amount', data=sales_Occupation)


# In[89]:


df.columns


# In[91]:


OrderNumber_Occupation= df.groupby(['Occupation'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='Occupation', y='Orders', data=OrderNumber_Occupation)


# In[92]:


# From the above graphs We can see that Sales in Amount and in Terms of Orders are leading by IT sector follows by Healthcare and Aviation. 


# In[93]:


# Product Category
ax = sns.countplot(data=df, x='State', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
    sns.set(rc={'figure.figsize':(15,5)}


# In[103]:


sns.set(rc={'figure.figsize':(15,5)}
ax=sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)


# In[97]:


sales_Product_category= df.groupby(['Product_Category'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='Product_Category', y='Orders', data=sales_Product_category)


# In[98]:


sales_Product_category= df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='Product_Category', y='Amount', data=sales_Product_category)


# In[105]:


#Above graph for Product category states that Number of orders are more in clothing, food and then Electronic gadgets but the amount spent is more on Fooding.


# In[106]:


# Sales of top 10 Products
sales_Product_id= df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(15)

sns.set(rc={'figure.figsize':(15,8)})
sns.barplot(x='Product_ID', y='Orders', data=sales_Product_id)


# In[101]:


df.columns


# In[107]:


# Final Conclusion 

#Most of the spending is attributed to individuals aged 26-35 who are married, employed in the IT sector, and reside in the states of Uttar Pradesh, Maharashtra, and Karnataka, respectively.
# and the product purchased by them most is Food followed by Clothing and Electronics gadgets. 


# In[ ]:




