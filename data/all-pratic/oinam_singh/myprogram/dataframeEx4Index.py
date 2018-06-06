import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(107)

outside =['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_idx=list(zip(outside,inside))
hier_idx=pd.MultiIndex.from_tuples(hier_idx)
print(hier_idx)
df=pd.DataFrame(np.random.randn(6,2),index=hier_idx,columns=['A','B'])
print(df)
print(df.loc['G1'].loc[1])
print(df.iloc[1])