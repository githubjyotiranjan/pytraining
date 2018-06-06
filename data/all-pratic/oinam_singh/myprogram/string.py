x="7"
print(x.isalnum())
print(x.isnumeric())
print(x.isalpha())

dics=[{'name':'oinam','age':35},{'name':'singh','age':23},{'name':'abc','age':18}]
dic={'name':'oinam','age':35}
print(dic.values())

list3 = ["a", "b", "c", "d"]
list2=list(list3)
list3.reverse()
print(list3)
print(list2)

tup1=(1,2,3,4,5)
s1={3,4}
s=set()
s.add(2)
s.add(s1)
print(s)

x=False
if x:
    print ("true")
else:
    print ("false")