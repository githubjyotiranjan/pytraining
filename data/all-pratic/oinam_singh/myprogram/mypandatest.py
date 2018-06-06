import pandas as pd

dic={'a':10,'b':20,'c':30}
my_list=[10,20,30]
#print(pd.Series(data=my_list))
my_label=['a','b','c']
ser1= pd.Series(my_list, my_label)
print(pd.Series(my_list, my_label))
print(ser1['a'])
ser2= pd.Series([1,2,3],index=['a','b','d'])
print (ser1+ ser2)
print (ser1*ser2)