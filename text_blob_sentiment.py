#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''


# In[2]:


blob = TextBlob(text)


# In[3]:


blob.tags  


# In[4]:


blob.noun_phrases 


# In[5]:


for sentence in blob.sentences:
    print(sentence.sentiment.polarity)


# In[18]:


testimonial = TextBlob("Textblob is worst to use")


# In[19]:


testimonial.sentiment


# In[ ]:




