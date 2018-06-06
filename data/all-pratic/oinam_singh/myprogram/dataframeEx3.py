import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(107)
df=pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())

newind='CA NY WY OR CO'.split()
df['States']=newind
print(df.set_index('States'))
#print(df)
#dd=df.reset_index()
#print(dd)
#print(df.set_index('States'))
