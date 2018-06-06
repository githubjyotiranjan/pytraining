
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


np.linspace(0,1,20)


# In[4]:


arr=np.arange(12,26)


# In[5]:


arr


# In[6]:


arr.reshape(4,3)


# reshape and append matrix

# In[14]:


arr1=np.arange(12,16)


# In[15]:


arr2=arr1+5


# In[16]:


arr2


# In[17]:


arr3=arr2+5


# In[18]:


arr3


# In[37]:


arr1=np.append([arr2],axis=0)
arr1


# In[41]:


arr4=np.append(arr1,arr2)
arr4


# In[48]:


arr_merge=np.append(arr1,arr2)
arr_merge


# In[51]:


arr_merge_1=np.append(arr_merge,arr3)
arr_merge_1.reshape(3,4)


# In[22]:


my_matrix = [arr1,arr2,arr3]
my_matrix


# Getting Sub Matrix-Matrix Selection

# In[24]:


mat_A = np.arange(1,26).reshape(5,5)
mat_A


# In[25]:


mat_A[1:2]


# In[26]:


mat_A[1:1]


# In[29]:


mat_A[:2,:2]


# In[70]:


matrix_A=np.arange(1,26).reshape(5,5)
matrix_A


# In[60]:


matrix_A[:3,1:2]


# In[67]:


matrix_A[3:5,0:5]


# get the standard deviation  of the values in matrix

# In[68]:


matrix_A.std()


# get the sum of the elements of a column in matrix-axis-0
# get the sum of the elements of a rows in matrix-axis-1
# 

# In[75]:


matrix_A.sum(axis=0)


# In[76]:


matrix_A.sum(axis=1)


# In[78]:


matrix_A.sum()


# Pandas-Other Mathematical Operation,Incremental things on numpy

# Series-Data Type (Kind of an array)

# In[79]:


import pandas as pd


# In[82]:


dic_1={"a":10,"b":20,"c":30}
dic_1.values()


# In[83]:


labels=["a","b","c"]
my_list=[10,20,30]
arr=np.array([10,20,30])


# In[84]:


pd.Series(data=my_list)


# In[85]:


pd.Series(data=my_list,index=labels)


# In[87]:


pd.Series(my_list,labels)


# In[90]:


pd.Series(arr,labels)


# In[93]:


pd.Series(dic_1)


# In[94]:


pd.Series(data=labels)


# In[96]:


ser1=pd.Series(data=[1,2,3,4],index=["USA","Germany","USSR","India"])
ser1


# In[98]:


ser2=pd.Series(data=[1,2,3,4],index=["USA","Italy","Japan","India"])
ser2


# In[99]:


ser1[1]


# In[101]:


ser1["India"]


# if two series are joint then it will club together matching values... if not find then NAN

# In[102]:


ser1+ser2


# DataFrame
# Seed--is used to get same response 

# In[112]:


import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(102)


# In[113]:


df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
df


# Selection and Indexing

# In[114]:


df['W']


# In[122]:


df[['W','X']]


# In[123]:


df.W


# In[124]:


type(df['W'])


# Adding a new column

# In[126]:


df['new']=df['W']+df['Y']
df


# In[133]:


df["Sub"]=df["W"]-df["X"]
df


# Selecting Columns

# In[135]:


df[["W","Sub"]]


# Removing Columns and Rows

# In[141]:


df1=df.drop("E",axis=0)
df1


# In[143]:


df2=df.drop("new",axis=1)
df2


# Deleting rows and columns permanently ...

# In[145]:


df.drop("new",axis=1,inplace=True)


# In[146]:


df


# In[147]:


df.drop("E",axis=0,inplace=True)
df


# Selecting Rows

# In[148]:


df.loc['A']


# In[149]:


df.loc[['A','B']]


# In[150]:


df.iloc[0]


# In[151]:


df.iloc[[0,3]]


# In[152]:


df.loc['B','W']


# In[163]:


df.loc[['B','W'],['B','Sub']]


# In[160]:


df.iloc[:3]


# Conditional Selectional

# In[164]:


df


# In[165]:


df>0


# In[166]:


df<0


# In[167]:


df[df>0]


# In[168]:


df[df<0]


# In[183]:


df[df['W']>0][['Y','Z']]


# In[186]:


df[(df['W']>0)&(df['Y']>0)]


# In[187]:


df[(df['W']>0)|(df['Y']>0)]


# In[190]:


df[(df['W']>0)&(df['Y']>0)][['W','Y']]


# Adding Column

# In[195]:


newind='Ca NY DR CD'.split()
newind


# In[196]:


df['state']=newind
df


# Reset Index

# In[197]:


df.reset_index()


# In[198]:


df.reset_index()


# In[199]:


df.index


# In[200]:


df.W


# In[207]:


df.set_index('state')


# Multi Level Index

# In[213]:


outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)


# In[214]:


hier_index


# In[215]:


df1=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
df1


# In[217]:


df1.loc['G1'].loc[3]


# In[218]:


outside=['G1','G1','G1','G2','G2','G2','G3','G3','G3']
inside=[1,2,3,1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
hier_index


# Groupby

# In[242]:


data={"Company":['GOOG','GOOG','MSFT','MFST','FB','FB'],"Person":['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],"Sales":[200,120,346,124,243,350]}
data


# In[243]:


df2=pd.DataFrame(data)


# In[244]:


df2


# In[245]:


df2.groupby('Company')


# In[246]:


g1=df2.groupby('Company')
g1


# In[247]:


g1.mean()


# In[248]:


df2.groupby('Company').mean()


# In[249]:


g1.Sales


# In[250]:


g1.sum()


# In[251]:


g1.std()


# In[252]:


g1.min()


# In[253]:


g1.describe()


# In[254]:


g1.describe().transpose()


# In[255]:


g1.describe().transpose()


# In[256]:


g1.describe().transpose()['GOOG']


# Merging,Joining, and Concatenating

# In[257]:


df1=pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']},index=[0,1,2,3])


# In[258]:


df2=pd.DataFrame({'A':['A4','A5','A6','A7'],'B':['B4','B5','B6','B7'],'C':['C4','C5','C6','C7'],'D':['D4','D5','D6','D7']},index=[4,5,6,7])


# In[259]:


df3=pd.DataFrame({'A':['A8','A9','A10','A11'],'B':['B8','B9','B10','B11'],'C':['C8','C9','C10','C11'],'D':['D8','D9','D10','D11']},index=[8,9,10,11])


# In[260]:


pd.concat([df1,df2,df3],axis=1)


# In[277]:


df_1=pd.DataFrame({'A':['A0','A1','A2','A3'],'B':['B0','B1','B2','B3'],'C':['C0','C1','C2','C3'],'D':['D0','D1','D2','D3']},index=[0,1,2,3])


# In[279]:


df_2=pd.DataFrame({'A_':['A4','A5','A6','A7'],'B_':['B4','B5','B6','B7'],'C_':['C4','C5','C6','C7'],'D_':['D4','D5','D6','D7']},index=[4,5,6,7])


# In[267]:


pd.merge(df_1,df_2,how="inner",on="key1")


# In[269]:


pd.merge(df_1,df_2,how="outer",on=["key1","key2"])


# In[280]:


df_1.join(df_2,how='outer')


# Info on Unique values

# In[281]:


df_1['A'].unique()


# In[282]:


df_1['A'].nunique()


# Value Count=Groupby(Count(Distinct))

# In[284]:


df_1['A'].value_counts()


# Selecting Data

# Applying Functions

# In[286]:


def times2(x):
    return x*2


# In[287]:


df_1['A'].apply(times2)


# In[288]:


df_1['A'].apply(times2)


# In[289]:


df_1.columns


# In[291]:


df_1.drop('A',axis=1)


# In[292]:


df_1.sort_values(by='C')#inplace=Flase by default


# In[293]:


df_1.isnull


# In[295]:


df.dropna()#Drops any NaN Values


# In[296]:


import numpy as np


# In[297]:


nullvaluesreplace=pd.DataFrame({'col1':[1,2,3,np.nan],'col2':[np.nan,np.nan,666,77]})
nullvaluesreplace


# In[298]:


nullvaluesreplace.head()


# In[300]:


nullvaluesreplace.fillna("Null")


# Data Input and Output

# In[309]:


import numpy as np
import pandas as pd


# In[320]:


readfile=pd.read_csv('Desktop/example')
readfile


# In[321]:


df.to_csv('Desktop/example1',index=False)


# In[334]:


readfile_csv=pd.read_csv('Desktop/ebay.csv')
readfile_csv


# In[335]:


readfile_user=pd.read_csv('Desktop/Python_Day3/ebay.csv')
readfile_user


# In[336]:


readfile_user=pd.read_csv('Desktop/Python_Day3/u.user')
readfile_user


# In[337]:


readfile_excel=pd.read_excel('Desktop/Python_Day3/Excel_Sample.xlsx',sheet_name='Sheet1')
readfile_excel


# In[338]:


readfile_excel.max()


# In[340]:


readfile_user.max()


# In[341]:


readfile_user.min()


# In[344]:


readfile_user.to_csv('Desktop/Python_Day3/u1.user')
readfile_user


# In[351]:


a=readfile_user.iloc[3]


# In[352]:


a


# In[353]:


readfile_user.iloc[:3]


# In[354]:


readfile_user.iloc[1:10]


# Read From Web Source

# In[356]:


ReadWebSourceData=pd.read_html("http://www.fdic.gov/bank/individual/failed/banklist.html")
ReadWebSourceData


# Database

# In[367]:


from sqlalchemy import create_engine
engine=create_engine('sqlite:///:memory:')
engine_1=create_engine('sqlite:///:memory:')


# In[358]:


df.to_sql('data',engine)


# In[361]:


sql_df=pd.read_sql('data',con=engine)


# In[362]:


sql_df


# In[370]:


readfile_user.to_sql('data',engine_1)

