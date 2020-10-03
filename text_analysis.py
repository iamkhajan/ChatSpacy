#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df=pd.read_csv('spam.csv',sep=',',encoding='latin-1')
df.columns
#selecting just interested coloumns
df=df[['v1','v2']]
#renaming coloumns to make more sense
df.rename(columns={'v1': 'Status', 'v2': 'Message'}, inplace=True)
df.head()
len(df)
len(df[df.Status=='spam'])

df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0
df.head()
cv = CountVectorizer()
df_x=df["Message"]
df_y=df["Status"]
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
x_traincv = cv.fit_transform(x_train)
a=x_traincv.toarray()
#cv.get_feature_names()
print(len(ax))
a[0]
cv.inverse_transform(a[0])
x_train.iloc[0]
x_testcv=cv.transform(x_test)
x_testcv.toarray()
mnb = MultinomialNB()
y_train=y_train.astype('int')
y_train
mnb.fit(x_traincv,y_train)
testmessage=x_test.iloc[0]
testmessage
predictions=mnb.predict(x_testcv)
predictions

a=np.array(y_test)
count=0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1

count
len(predictions)




