
# coding: utf-8

# In[3]:


import numpy as np
np.ones(10)*5


# In[4]:


np.arange(10,50)


# In[6]:


np.arange(0,9).reshape(3,3)


# In[8]:


np.eye(3)


# In[9]:


np.random.rand(4)


# In[10]:


np.arange(1,101).reshape(10,10)/100


# In[11]:


np.linspace(0,1,20)


# In[16]:


np.arange(12,24).reshape(3,4)


# In[24]:


array1 = np.arange(1,26).reshape(5,5)
print(array1)
print(array1[:2,:2])


# In[25]:


mat


# In[34]:


array1 = np.arange(11,26).reshape(3,5)
print(array1)
print(array1[0:,1])


# In[36]:


array1 = np.arange(11,26).reshape(3,5)
print(array1)
print(array1[:3,1:2])


# In[41]:


array1 = np.arange(11,26).reshape(3,5)
print(array1)
print(array1[2:,0:5])


# In[45]:


array1 = np.arange(11,26).reshape(3,5)
np.sort(array1)
np.std(array1)
np.sum(array1)


# In[46]:


mat.sum(axis=0)


# In[47]:


mat.sum(axis=1)


# Pandas
# 

# In[48]:


labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30} 


# In[49]:


import pandas as pd


# In[50]:


pd.Series(data=my_list)


# In[52]:


pd.Series(data=my_list,index=labels)


# In[53]:


pd.Series(my_list,labels)


# In[54]:


pd.Series(arr)


# In[55]:


pd.Series(arr,labels)


# In[56]:


pd.Series(d)


# In[57]:


pd.Series(data=labels)


# In[58]:


import pandas as pd


# In[60]:


ser = pd.Series((1,2,3,4,5),index=['USA','GERMANY','Italy','Japan','India'])


# In[63]:


ser1 = pd.Series(my_list)
ser2 = pd.Series(my_list)
ser1+ser2


# In[68]:



df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(),columns='W X Y Z'.split())
df


# In[72]:


np.random.seed(100)


# In[73]:


np.random.randn()


# In[106]:


df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(),columns='W X Y Z'.split())


df.loc[['A','B'],['W','Y']]
df.loc['A':,'X']


# In[75]:


df['W']


# In[76]:


df[['W','Z']]


# In[78]:


df.W


# In[79]:


type(df['W'])


# In[81]:


df['new'] = df['W']+df['Y']
df


# In[85]:


df['old'] = df['W']+df['Y']+df['Y']
df


# In[87]:


df['old2']=df['W']*43
df


# In[89]:


df[['W','Z']]


# In[100]:



df.iloc['W','X']


# In[98]:


df.drop('X',axis=0,inplace=True)


# In[99]:


df.loc['A']


# In[107]:


df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(),columns='W X Y Z'.split())
df


# In[108]:


df>0


# In[119]:


df = pd.DataFrame(np.random.randn(5,4)*10, index='A B C D E'.split(),columns='W X Y Z'.split()


# In[120]:


df[df['W']<0]


# In[121]:


df[df['W']>0]['Y']


# In[123]:


df[(df['X']>0.5) & (df['Y']>0.5)]


# In[124]:


df.reset_index()


# In[126]:


df = pd.DataFrame(np.random.randn(5,4)*10,)


# In[131]:


states=['AP','UP','fg','hj']
#df.set_index(states)


# In[137]:


outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index


# In[138]:


hier_index
df = pd.DataFrame(np.random.randn(6,2), index=hier_index,columns=['A','B'])
df


# In[139]:


df.loc['G1'].loc[1]


# In[143]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person' :['Sam','charlie','Amy','Vanessa','Car','sarah'],
        'Sales'  :[200,12,456,340,124,243]
       }
df = pd.DataFrame(data)


# In[146]:


by_comp = df.groupby('Company')
by_comp.mean()


# In[152]:


by_comp.count()
by_comp.sum()
by_comp.describe()


# In[155]:


by_comp.describe().transpose()['GOOG']


# In[159]:


df1= pd.DataFrame({'A':['1','2','3','4'],
                  'B':['B0','B1','B2','B4'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']},
                 index=[0,1,2,3])


# In[160]:


df2= pd.DataFrame({'A':['A4','A5','A6','A7'],
                  'B':['B4','B5','B6','B7'],
                  'C':['C4','C5','C6','C7'],
                  'D':['D4','D5','D6','D7']},
                 index=[4,5,6,7])


# In[161]:


df3= pd.DataFrame({'A':['A8','A9','A10','A11'],
                  'B':['B8','B9','B10','B11'],
                  'C':['C8','C9','C10','C11'],
                  'D':['D8','D9','D10','D11']},
                 index=[8,9,10,11])


# In[178]:


df1['A'].unique()
df1['A'].nunique()


# In[180]:


def times2(x):
    return x*2


# In[181]:


df1['A'].apply(times2)


# In[163]:


pd.concat([df1,df2,df3],axis=1)


# In[172]:


df1= pd.DataFrame({'A':['A0','A1','A2','A'],
                  'B':['B0','B1','B2','B'],
                  'C':['C0','C1','C2','C'],
                  'D':['D','D','D','D']},
                 index=[0,1,2,3])

df2= pd.DataFrame({'A':['A4','A5','A6','A'],
                  'B':['B4','B5','B6','B'],
                  'C':['C4','C5','C6','C'],
                  'E':['D','D','D','D']},
                 index=[0,1,2,3])

pd.merge(df1,df2,how='inner',on=['D','D'])


# In[166]:


pd.merge(df1,df2,how='outer',on=['D','D'])


# In[173]:


df1.join(df2)


# In[174]:





# In[185]:


df= pd.read_csv('example')


# In[187]:


pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# In[188]:


df.to_csv('example',index='false')


# In[ ]:


df.to_excel('Excel')


# In[193]:


df= pd.read_csv('u.user')


# In[191]:


print(df)

