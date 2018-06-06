import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(107)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
#print(df)
#print(df['W'])
#print(type(df['W']))
#print(df[['W','Z']])

df['newX']=df['X']+df['X']*.01
print(df)

dd=df.drop('newX',axis=1)
print(dd)

##inplace=True take the action permanently

#ddp=df.drop('newX',axis=1,inplace=True)
ddp=df.drop('newX',axis=1)

print(ddp)
print(df)

#ddd=df.drop('A',axis=0,inplace=True)
#print(ddd)
#print(df)

print(df.loc['B'])

print(df.iloc[2])

#subset
print(df.loc['B','Y']) #display B Y location

print(df.loc[['A','B'],['Z','Y']]) #display A,B and Z,Y location matrix values

print(df.iloc[[0]])
print(df.iloc[[0][0]])
print(df.iloc[[0,1]])