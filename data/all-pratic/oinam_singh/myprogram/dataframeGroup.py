import pandas as pd
import numpy as np

data={'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
      'Person':['Same','Charlie','James','Tom','Kiran','Sam'],
      'Sales':[200,120,300,400,250,750]}
df=pd.DataFrame(data)
by_company=df.groupby('Company')
#print(by_company)
print(df.groupby('Company').mean())
print(df.groupby('Company').sum())
print(df.groupby('Company').std()) #std standard deviation
print(by_company.describe().transpose())
print(by_company.describe().transpose()['GOOG'])