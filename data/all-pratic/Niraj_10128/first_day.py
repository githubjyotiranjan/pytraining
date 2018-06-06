
# coding: utf-8

# In[8]:


class Dog:
    nature = 'they are vary agressive'
    name=''


# In[9]:


dog1 = Dog()
dog1.name='TOM'
dog2 = Dog()
dog2.name='BOX'
dog3 = Dog()
print(dog1.name)
print(dog2.name)
print(dog1.nature)


# In[22]:


class Cat:
    def __init__(self,name,age,teeth):
        self.name=name
        self.age=age
        self.teeth=teeth
dog1=Cat("TOMMY","3","5")
print(dog1.name)
print(dog1.age)


# In[18]:


class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)


# In[38]:


import numpy as np
arr = np.arange(0,10)
print(arr+arr)
print(arr-arr)
print(arr*arr)
print(arr/arr)
#print(1/arr)
print(np.sqrt(arr))
print(np.exp(arr))
print(np.max(arr))
print(np.min(arr))
print(np.average(arr))
print(np.count_nonzero(arr))
print(np.sin(arr))


# In[41]:


arr = np.arange(1,10)
arr
np.log(arr)


# In[42]:


my_list = [1,2,3]
my_list
np.array(my_list)


# In[44]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix
np.array(my_matrix)


# In[50]:


my_matrix = np.arange(-20,20,2).reshape(2,10)
print(my_matrix)


# In[51]:


my_list = np.ones(3)
my_list


# In[52]:


mylist = np.ones(9).reshape(3,3)
print(mylist)


# In[53]:


np.linspace(0,10,50)


# In[54]:


np.eye(4)


# In[56]:


np.random.rand(4)


# In[57]:


np.random(1,100)


# In[58]:


np.random.randn(5,5)


# In[59]:


np.random.randint(1,100)


# In[60]:


np.random.randint(1,100,10)


# In[61]:


np.random.randint(1,100,10)


# In[74]:


mymatrix = np.random.randint(1,100,20)
print(mymatrix)
np.argmin(mymatrix)
np.argmax(mymatrix)
print(mymatrix.shape)
print(mymatrix.reshape(5,4))
print(arr.dtype)


# In[75]:


np.random.randn(5,5)

