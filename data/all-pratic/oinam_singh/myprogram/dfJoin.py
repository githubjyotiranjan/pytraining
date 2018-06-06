import pandas as pd

data1={'key1':['A0','A0','A1','A2'],
      'key2':['A0','A1','A0','A1'],
      'B':['B0','B1','B2','B3'],
      'C':['C0','C1','C2','C3'],
      'D':['D0','D1','D2','D3']}
dfleft=pd.DataFrame(data1)

data2={'key1':['A0','A1','A1','A2'],
      'key2':['A0','A0','A1','A1'],
      'B':['B4','B5','B6','B7'],
      'C':['C4','C5','C6','C7'],
      'D':['D4','D5','D6','D7']
      }
dfright=pd.DataFrame(data2)

dcon1=pd.merge(dfleft,dfright,how="outer",on=['key1'])
print(dcon1)

print(dfleft.join(dfright, lsuffix='_l'))

left = pd.DataFrame({'key': ['foo', 'bar'], 'val': [1, 2]}).set_index('key')
right = pd.DataFrame({'key': ['foo', 'bar'], 'val': [4, 5]}).set_index('key')
t=left.join(right, lsuffix='_l', rsuffix='_r')
print(t)



