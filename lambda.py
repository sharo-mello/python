#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = lambda a,b : a+b
print(a(3,5))


# In[3]:


multiply = lambda a,b : a*b
print(multiply(2,3))


# In[4]:


def lamdafunc(n):
    return lambda a : a*n

b = lamdafunc(3)
print(b(4))


# In[ ]:




