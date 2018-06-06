
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


print(hello world)


# Arithmetic Operations

# In[1]:


2+4


# In[2]:


5/2 


# In[3]:


5//2


# In[4]:


5**2


# In[5]:


2+4
5/2


# In[6]:


-2-6


# In[7]:


5//2+3-2


# In[8]:


3*1**3


# In[9]:


6-(3-2)**3


# In[10]:


7//(2+1)/2


# In[11]:


0.3%


# In[12]:


9-{5*(5-2)}


# In[13]:


9-(5*(6-2))


# Variable Assignment
# Numeric Assignment
# There is no need to specify the data type....
# Int+Int=Int
# Int+Float=Float
# Float+Float=Float
# 

# In[14]:


a=2
a/2


# In[15]:


a=5
b=9
a+b


# In[16]:


a=5.5
b=2


# In[17]:


a//b


# In[18]:


a/b


# In[19]:


a+1.5


# Variable Assignment
# String  Assignment

# In[20]:


c="Hello World"


# In[21]:


c


# In[22]:


print(c)


# In[23]:


print('Hello World')


# In[24]:


c='Hello World'
c


# In[25]:


c="Hi"


# In[26]:


d='How are you?'


# In[27]:


print(c d)


# In[28]:


c d


# In[29]:


c


# In[30]:


d


# In[31]:


print (c+d)


# In[32]:


c+" "+d


# In[33]:


Income=5000


# In[34]:


Tax=5000*0.1
Tax


# In[35]:


print("The Tax is"+Tax )


# In[36]:


print(tax)


# In[37]:


print(Tax)


# In[38]:


print("Tax is:" Tax)


# In[39]:


Tax=Income*0.1
Tax


# In[40]:


print("The tax is:{}").format(Tax)


# In[42]:


print("The Tax is:" Tax)


# In[41]:


print "The Tax is:" Tax


# In[43]:


py=3.14
radius=5
area=py*radius*2
print(area)


# In[44]:


round(3,2)


# Arithmetic Functions

# In[45]:


a=5/3


# In[46]:


round(a,2)


# In[68]:


a=int(5/2)
a


# In[48]:


a=int(5/2)
a


# In[49]:


float(a)


# a.<tab button>-All possible commands
#     '''For Commenting

# String -----How to eliminate the error for ' and "

# In[50]:


Mystory='i Don't like eat cheese'
print(Mystory)


# In[55]:


Mystory='i Don\'t like to  eat cheese'
print(Mystory)


# In[56]:


Mystory="I Don't like to eat "Cheese""
print(Mystory)


# In[60]:


Mystory="I Don\'t like to eat \"Cheese"
print(Mystory)


# Formatting the output-String,Numbers and Variables

# In[61]:


name="Mahesh"
age=35


# In[64]:


print('My Name:{one} and my age is:{two}'.format(one=name,two=age))


# In[65]:


print('My Name:{} and my age is:{}'.format(name,age))


# In[67]:


print('Tax is:{}'.format(Tax))


# In[70]:


print("Hello\n"*3)


# In[71]:


print("Hello\n"*3+"The End")


# In[72]:


"Nick".upper()


# In[73]:


len("helloworld")


# In[74]:


"Hi my name is Manish".replace("Manish","Sumit")


# In[87]:


Bob="my Name is Manish\n"*3
print(Bob)


# In[89]:


BobNew=Bob.replace("Manish","Sumit")
print(BobNew)


# In[92]:


BobNew="Hellow"
x1=BobNew.capitalize
print(x1)


# In[93]:


x1=BobNew.casefold
print(x1)


# In[94]:


x1=BobNew.center
print(x1)


# In[105]:


x1="Hi I am here"


# In[106]:


x1.find("I")


# In[107]:


x1.split


# Comparator Operator

# In[108]:


2==3


# In[109]:


5/2>3


# In[111]:


a=6%3==0
a


# In[112]:


a=6%3<>0
a


# In[114]:


a=6%3!=0
a


# Logical Operator

# In[123]:


6%3!=0 or 6%3==0


# Input

# In[124]:


age=input("Enter Your age")


# In[125]:


print(age)


# In[137]:


radius=int (input("Enter thye radius"))


# In[138]:


radius


# In[135]:


py=3.14


# In[139]:


area=py*radius*2


# In[140]:


print(area)


# In[144]:


pi=3.14
radius=int (input("Enter thye radius"))
area=pi*radius*2
print(area)


# In[152]:


Salary=int (input("Enter the Salary: "))
Tax=int (input("Enter the Tax slab: "))
Tax=Tax/100
NetAmount=int(Salary-Salary*Tax)
print('Net Amount given to the employee is:{}'.format(NetAmount))


# Format

# In[164]:


float = 134.5555555
print("Float number %f"%(float) )


# In[165]:


print("here is the number %d.Here is the string %s"%(123,"hi"))


# In[170]:


a=30
b=20
print("The addition of %d and %d is:\n %d"%(a,b,a+b))


# Indexing

# In[171]:


x="Hello World"
x[0]


# In[174]:


i=int(input("Enter the Index"))
x[i]


# Slicing

# In[175]:


x[:]


# In[176]:


x[i:]


# In[180]:


i=int(input("Enter the Index"))
x[:i]


# In[181]:


i=int(input("Enter the Index"))
x[i:]


# In[182]:


y=x[6:9]
y


# In[185]:


x.capitalize()


# In[187]:


x.isalpha()


# In[193]:


x.center(1)


# Collections

# LIST

# In[202]:


List1=[1,2,"hi","str"]
List1


# In[203]:


List2=[123,List1]


# In[204]:


List2


# In[206]:


List2[0]


# In[209]:


List2[1]


# In[211]:


List2[1:]


# In[212]:


List2[0:]


# In[213]:


List1[2]=5


# In[214]:


List1


# In[215]:


List2[1][2]


# DICTIONARY

# In[218]:


D1={1:"Ram",2:List1,3:"Hi",4:123}
D1


# In[217]:


D1[2]


# In[222]:


D1[1]


# In[223]:


D1.keys()


# In[224]:


D1.values()


# In[228]:


D1[2][0]


# In[233]:


List1.append(5)


# In[235]:


List1.append(987)


# In[239]:


List1.pop()


# In[243]:


List1.reverse()


# In[244]:


List1


# In[253]:


myList=[78,5,8,98]


# In[254]:


myList.sort()


# In[255]:


myList


# In[256]:


tup1=(4,6,7)


# In[257]:


tup1


# In[262]:


tup1.count(7)


# In[261]:


tup1.index(6)


# In[263]:


tup2=(2,4)
tup3=tup1+tup2


# In[264]:


tup3


# In[265]:


len(tup3)


# In[266]:


4 in tup3


# In[267]:


tup3.count(4)


# In[268]:


max(tup3)


# In[269]:


tup3[2:5]


# In[270]:


set1={1,4,67,97}


# In[271]:


set1


# In[272]:


len(set1)


# In[273]:


max(set1)


# In[274]:


min(set1)


# In[275]:


3 in set1


# In[276]:


set2={34,56}
set1.update(set2)


# In[277]:


set1


# In[278]:


x=set()


# In[279]:


x.add(5)


# In[280]:


x.add(7)


# In[281]:


x


# In[282]:


x.add(10)


# In[283]:


x.add("hi")


# In[284]:


x


# In[286]:


x.discard(3)


# In[287]:


x


# In[288]:


x.discard('hi')


# In[289]:


x


# Control Statement-If Else

# In[299]:


a=5
b=5
if a>b:
 print(a)
elif a==b:
 print(a+b)
else:
 print(b)


# In[305]:


Salary=int (input("Enter the Salary: "))
if 50000>Salary>40000:
 Tax=30
elif 40000>Salary>30000:
 Tax=20
elif 30000>Salary>20000:
 Tax=10
else:
 Tax=5
NetAmount=int(Salary-Salary*Tax/100)
print('Tax for the employee is:{}%'.format(Tax))
print('Tax paid by the employee is:{}'.format(Salary*Tax/100))
print('Net Amount given to the employee is:{}'.format(NetAmount))


# In[306]:


Salary=int (input("Enter the Salary: "))
if 10000<Salary<20000:
 Tax=3
elif 20000<Salary<30000:
 Tax=5
elif 30000<Salary<40000:
 Tax=10
else:
 Tax=20
NetAmount=int(Salary-Salary*Tax/100)
print('Tax for the employee is:{}%'.format(Tax))
print('Tax paid by the employee is:{}'.format(Salary*Tax/100))
print('Net Amount given to the employee is:{}'.format(NetAmount))


# In[322]:


x='world'
y=x
y
reversed(y)







# In[323]:


y


# In[327]:


var=int(input("Enter how many prints you want"))
for i in range(0,var):
    print(var)

