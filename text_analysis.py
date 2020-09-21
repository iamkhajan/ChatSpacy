#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# In[32]:


df=pd.read_csv('spam.csv',sep=',',encoding='latin-1')


# In[33]:


df.columns


# In[34]:


#selecting just interested coloumns
df=df[['v1','v2']]


# In[35]:


#renaming coloumns to make more sense
df.rename(columns={'v1': 'Status', 'v2': 'Message'}, inplace=True)


# In[36]:


df.head()


# In[37]:


len(df)


# In[38]:


len(df[df.Status=='spam'])


# In[39]:


df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0


# In[41]:


df.head()


# In[44]:


cv = CountVectorizer()
df_x=df["Message"]
df_y=df["Status"]


# In[45]:


x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


# In[49]:


x_traincv = cv.fit_transform(x_train)


# In[52]:


a=x_traincv.toarray()


# In[65]:


#cv.get_feature_names()
print(len(ax))


# In[66]:


a[0]


# In[70]:


cv.inverse_transform(a[0])


# In[69]:


x_train.iloc[0]


# In[71]:


x_testcv=cv.transform(x_test)
x_testcv.toarray()


# In[72]:


mnb = MultinomialNB()


# In[73]:


y_train=y_train.astype('int')


# In[74]:


y_train


# In[75]:


mnb.fit(x_traincv,y_train)


# In[85]:


testmessage=x_test.iloc[0]


# In[86]:


testmessage


# In[77]:


predictions=mnb.predict(x_testcv)


# In[78]:


predictions


# In[79]:


a=np.array(y_test)


# In[80]:


a


# In[81]:


count=0


# In[82]:


for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1


# In[83]:


count


# In[84]:


len(predictions)


# In[ ]:




