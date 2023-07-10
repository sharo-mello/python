#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func1(a,b):
    print("add",a+b)
func1(2,8)


# In[3]:


def func2(*kids):
    print(kids[2])
func2("Ram","Sharo","Melloo")


# In[6]:


def kids(kid1,kid2,kid3):
    print(kid3)
kids(kid1="sharo",kid2="ram",kid3="mello")


# In[9]:


def func3(**kid):
    print("lname of kid is",kid["lname"])
    
func3(fname="sharo",lname="mello")


# In[ ]:




