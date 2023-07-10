#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=3
b=5

if b<a:
    print("b is less than a")
elif b==a:
    print("both are same")
else:
    print("b greater than a")


# In[2]:


#short hand if

print("A greater than b ") if a>b else print("b greater than a")


# In[4]:


print("a greater than b") if a>b else print("A equals to B") if a==b else print("b greater than a") if b>a else()


# In[8]:


#AND operator

print("both conditions are True") if b>a and a>2 else()


# In[9]:


#OR 

print("any one conditions passed") if b>a or a>b else()


# In[10]:


#nested if 

if a<b:
    if a>0:
        print("both are greater than 0")
    else:
        pass


# In[ ]:




