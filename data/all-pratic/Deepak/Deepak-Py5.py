
# coding: utf-8

# # Program to check if teh input string is same as expected

# In[1]:


class LetsPlay:
    LifeLeft = 0
    wordlength = 0

    def __init__(self, word):
        self.word = word
        LetsPlay.LifeLeft = 10

    def getresult(self):
     num = 0
     wordlen = len(self.word)
     for i in range(0, wordlen):
        inputletter: str = input("enter letter: ")
        arr = list(self.word)
        for j in range(num, len(arr)):
                if inputletter == arr[j]:
                    num += 1
                    break
                else:
                    LetsPlay.LifeLeft = LetsPlay.LifeLeft-1
                    print("wrong number , try again life left {}", LetsPlay.LifeLeft)
                    break
        break
test = LetsPlay("deepak")
test.getresult()


# In[4]:


import numpy as np
arr=np.arange(0,50)


# In[8]:


arr=np.arange(10,51)


# In[9]:


arr


# In[11]:


np.ones((1,10))*5


# In[13]:


np.eyes(1,2)


# In[23]:


arr = np.arange(9).reshape(3,3)

arr


# In[32]:


np.eye(3)


# In[30]:


np.random.rand(1)


# In[41]:


arr = np.arange(0,1,.01)
arr.reshape(10,10)


# In[46]:


arr = np.arange(0,1,.05)
arr


# In[54]:


np.linspace(0,1,20)


# In[56]:


np.arange(12,25).reshape(3,4)


# In[75]:


arr = np.eye(3)
arr[1:,:3]


# In[78]:


arr = np.arange(1,26).reshape(5,5)


# In[100]:


arr[1:4,1:3]


# In[85]:


arr(1:,:1)


# In[109]:


arr = np.arange(12,27).reshape(3,5)
arr


# In[114]:


arr= np.arange(2,13,5).reshape(3,1)
arr


# In[117]:


np.arange(16,26,1).reshape(2,5)


# In[120]:


arr = np.arange(16,26,1).reshape(2,5)


# In[121]:


arr.std()


# In[122]:


arr.cumsum()


# In[123]:


arr.sum(axis=0)


# In[124]:


arr.sum(axis=1)


# In[126]:


d= {'a':1,'b':2,'c':3}
d.values()


# In[137]:


import pandas as pd
my_list = [10,20,30]
labels = ['aa','bb','cc']
arr = np.array([10,20,30])
d= {'a':1,'b':2,'c':3}


# In[131]:


pd.Series(data=my_list)


# In[135]:


pd.Series(data=my_list, index =labels)


# In[139]:


pd.Series(data=d)


# In[142]:


pd.Series(arr,labels)


# In[146]:


series1 = pd.Series(data=my_list, index =['USA','India','China'])


# In[150]:


series2 = pd.Series(data=[12,56,87], index =['USA','India','Russia'])


# Ordered pair

# In[151]:


series1 + series2


# # DataFrame: for getting data from excelsheets
# 

# In[159]:


from numpy.random import randn
arr = np.random.seed(118) # seed: to have the same sequecnce in the team fo common opeartion


# In[160]:


df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df


# selection and indexing
# 

# In[163]:


df['W']


# In[169]:


df[['W','Z']]


# In[170]:


df['AA'] = df['W'] + df['Z']


# In[171]:


df


# In[176]:


df['AB'] = df['W']*2


# In[178]:


df['Y'] = df['Y']/2


# In[179]:


df


# In[180]:


df.drop('AB', axis=1) #it will delete in memory not permanent


# In[183]:


df.drop('AB', axis=1, inplace=True) # it will delete permanently


# In[184]:


df


# In[185]:


df.drop('E', axis=0)


# subset row and column
# 

# In[186]:


df.loc[['A','B']]


# In[187]:


df.loc[['A','B'],['W','Z']]


# In[200]:


df.loc[['W','Z']]


# Conditional check

# In[201]:


df>0


# In[202]:


df[df>0] # tabular form 


# In[204]:


df[df['W']< 0] # tabular form select rows  where w<0


# In[207]:


df[df['W']> 0][['X','Y']]


# In[214]:


df[(df['W']> 0) & (df['X']> 0)] # and operation bitwaise &


# In[215]:


df[(df['W']> 0) | (df['X']> 0)] # or operation bitwise |


# create index on fly adding new index

# In[216]:


newStates = 'MP UP HP DL KA'.split()
df['states'] = newStates
df


# In[217]:


df.set_index('states') # to put a primary key


# In[221]:


df.set_index('states')


# Multilevel index #level

# In[222]:


list1 = ['a','a','a','b','b']
list2 = [1,2,3,1,2,3]

hindex = list(zip(list1,list2))
hindex = pd.MultiIndex.from_tuples(hindex)
hindex


# In[224]:


df = pd.DataFrame(np.random.randn(5,2),index = hindex, columns=['A','B'])
df


# In[225]:


df.loc['a']


# In[227]:


df.loc['a'].loc[1]


# groupby

# In[228]:


data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'], 
      'Person':['Sam','Charlie','Amy', 'Vanessa','Carl','Sarah'],
     'Sales':[200,120,340,124,243,350]}


# In[229]:


df=pd.DataFrame(data)


# In[230]:


df


# In[233]:


by_company = df.groupby('Company')


# In[237]:


by_company.mean()


# In[238]:


by_company.std()


# In[239]:


by_company.describe()


# In[240]:


by_company.describe().transpose() ##pivot


# In[242]:


by_company.describe().transpose()['GOOG']

