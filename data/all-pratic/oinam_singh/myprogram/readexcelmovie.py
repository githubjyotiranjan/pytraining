import pandas as pd
import numpy as np
df=pd.read_csv("E:/testprogram/u.user",sep='|')
#print(df)
file_name="E:/testprogram/newfile1.csv"
df.to_csv(file_name, sep='|')