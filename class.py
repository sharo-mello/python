#!/usr/bin/env python
# coding: utf-8

# In[1]:


class myclass():
    x = 5
a=myclass
print(a.x)


# In[6]:


class person:
    def __init__(self,name,role,age):
        self.name=name
        self.role=role
        self.age=age
    def getlist(self):
        print("myname is {0} aged {2}, working as a {1}".format(self.name,self.role,self.age))
        
employee = person("Sharo","Performance Engineer",24)
employee.getlist()
        


# In[ ]:




