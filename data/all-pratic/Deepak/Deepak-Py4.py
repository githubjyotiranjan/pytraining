
# coding: utf-8

# In[1]:


try:    
    userInput = int(input("Please enter the number until which you want to print odd numers : "))
    for i in range(0,userInput):        
        if(i % 2 !=0):
            print(i)
except:
        print("number is incorrect")


# In[2]:


sum = lambda num1, num2: num1+num2
print("sum of values is", sum(10,20))


# In[3]:


import numpy as np
arr = np.arange(0,10)
print(arr)


# In[4]:


arr*arr


# In[5]:


arr**arr


# In[6]:


arr/arr


# In[7]:


1/arr


# In[8]:


arr


# In[9]:


np.log(arr)


# In[10]:


matrix = [[1,2,3],[4,5,6],[7,8,9]]
np.array(matrix)


# In[11]:


np.arange(0,50,5)


# In[12]:


np.arange(100.01,2000.00,100.99)


# In[13]:


np.zeros((5,5,8))


# In[14]:


np.ones((2,3))


# In[15]:


arr = np.ones((2,3))
arr*5


# In[16]:


np.linspace(0,10,25)


# In[17]:


np.random.rand(2)


# In[18]:


np.random.rand(1000000000)


# In[19]:


np.random.randn(100)


# In[20]:


np.random.randn(20,100)


# In[21]:


np.random.randint(1,100,10)


# In[22]:


np.random.rand(1,100,10)


# In[23]:


arr.arange(0,50,10)


# In[25]:


arr=np.arange(0,50,10)
arr


# In[24]:


arr.reshape(2,3)


# In[29]:


arr=np.arange(0,50)


# In[30]:


arr.reshape(2,3)


# In[31]:


arr.max()


# In[32]:


arr.argmax()


# In[33]:


arr=np.arange(0,50,10)


# In[34]:


arr.max()


# In[35]:


arr.argmax()


# In[36]:


arr


# In[37]:


arr.reshape(5,1)


# In[38]:


arr.reshape(1,5)

