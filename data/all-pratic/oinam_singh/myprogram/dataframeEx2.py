import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(107)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

#print(df.iloc[[0][0]])
#print(df.iloc[[0]])
#print(df.iloc[[0,1]])

#print(df[df>0]) #only positive values of df
print(df)
print(df[df['W']>0]) #only positive values of df['W']

print(df[df['W']>0]['Y']) #
print(df[df['W']>0][['Y','Z']]) #

print(df[(df['W']>0) & (df['X']>0)])
print(df[(df['W']>0) | (df['X']>0)])

print(df[(df['W']>0) ^ (df['X']>0)])