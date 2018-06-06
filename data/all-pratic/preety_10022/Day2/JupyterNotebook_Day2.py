
# coding: utf-8

# In[4]:


import numpy as np
arr =np.arange(0,10)


# In[3]:


arr


# In[4]:


arr+arr


# In[5]:


arr*arr


# In[6]:


arr**arr


# In[7]:


arr//arr


# In[8]:


arr-arr


# In[11]:


arr/arr


# In[12]:


1/arr


# In[14]:


np.sqrt(arr)


# In[15]:


np.sin(arr)


# In[16]:


np.tan(arr)


# In[17]:


np.log(arr)


# In[18]:


list=[1,5,6]
list


# In[19]:


np.array(list)


# In[20]:


my_matrix = [[1,6,7],[2,5,6]]
my_matrix


# In[21]:


np.array(my_matrix)


# Return evenly spaced values within a given interval

# In[22]:


element=np.arange(0,100,5)


# In[23]:


element


# Zeroes and Ones

# In[24]:


np.zeros(3)


# In[28]:


a=np.ones((3,3))
a


# In[38]:


np.linspace(0,10,50)


# In[39]:


np.eye(4)


# In[40]:


np.random.rand(2)


# In[41]:


np.random.rand(7,7)


# In[45]:


np.random.randn(2)


# In[46]:


np.random.randn(5,2)


# In[49]:


np.random.randint(1,100)


# In[52]:


np.random.randint(1,100,10)


# Reshape------------------

# In[9]:


arr1=np.arange(25)
arr1


# In[54]:


arr1


# In[5]:


arr2=np.random.randint(0,50,10)
arr2


# In[60]:


arr1.reshape(5,5)


# In[61]:


arr2.reshape(2,5)


# In[62]:


arr2.reshape(5,2)


# argmin and argmax is used to find the index or position of min and max.

# In[63]:


arr2.max()


# In[64]:


arr1.min()


# In[65]:


arr2.argmin()


# In[66]:


arr2.argmax()


# In[6]:


arr2.shape


# dtype

# In[7]:


arr2.dtype


# In[10]:


arr1.dtype

