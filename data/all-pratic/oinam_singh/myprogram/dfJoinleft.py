import pandas as pd

data1={'key1':['A0','A0','A1','A2'],
      'key2':['A0','A1','A0','A1']
      }
dfleft=pd.DataFrame(data1)

data2={
      'B':['B4','B5','B6','B7'],
      'C':['C4','C5','C6','C7'],
      'D':['D4','D5','D6','D7']
      }
dfright=pd.DataFrame(data2)


print(dfleft.join(dfright))





