
# coding: utf-8

# In[2]:


#Print World
print("Hello World")


# In[4]:


#Operator
#Mathemetical operation
''' 
+
-
*
//
**
% 
'''



# In[5]:


2+2


# In[6]:


4-2


# In[7]:


5*4


# In[8]:


5/2


# In[9]:


5//2 #integral division


# In[10]:


5**3 #5*5*5


# In[11]:


2+3*5+10/2 #bodmas rule


# In[12]:


6-(3**2)/8 #bodmas rule


# In[13]:


3.0/2


# In[14]:


#Variable assignment
a=2


# In[15]:


a


# In[16]:


a*50


# In[54]:


print('hello' * 3)


# In[22]:


c = "Hello World"


# In[23]:


c


# In[25]:


print(c)


# In[26]:


"hello let't try this one"


# In[27]:


#Tax calulation
personal_income = 100000
tax = personal_income*10/100
print(tax)


# In[28]:


#Area of a circle
pi = 3.14
radious = 5
area = pi*radious**2
print (area)


# In[29]:


round(78.5)


# In[30]:


round(1.666666,2)


# In[31]:


round(1.666666,3)


# In[32]:


round(1.666666,-2)


# In[33]:


#Type Conversion
int(5.9)


# In[34]:


float(5)


# In[35]:


a = str(5)


# In[36]:


a


# In[39]:


a = int(a)


# In[38]:


a


# In[41]:


# "",'' and escape sequence
''' 
\a: alert
\b: backspace
\cx: Control X
\e: escape
\f: Form feed
\n: New line or next line
\r: carriage return
\s: space
\t: tab
\v: Vertical Tab '''
mystory = 'I don't like to eat cheese'


# In[46]:


mystory = "I don't like to eat cheese"
print(mystory)


# In[47]:


mystory = "I don't like to eat \"cheese\""
print(mystory)


# In[98]:


print('Alone we can\ndo little;\nTogether we can\ndo more.')

#Concatination operator
a = "Sachin"
b = "Tendulkar"
c = a+' '+b
print(c)
# In[51]:


#Formated statement
name =  'Jyotiranjan'
age = 30
print('My name:{one} and my age is {two}'.format(one=name,two=age))


# In[52]:


name =  'Jyotiranjan'
age = 30
print('My name:{} and my age is {}'.format(name,age))


# In[92]:


print ('Here is your name: %s. Here ia your age %s' %('abc',30))


# In[53]:


#
name =  'Jyotiranjan'
age = 30
print('My name:{} and my age is {}'.format(name,age))print(3 * 'hello')


# In[59]:


#basic Methods and Functions
print ("Nick".upper())
print(len("hello World"))
print("Hi my name is Manish".replace("Manish","Singh"))


# In[62]:


abc = "test"
print(abc);
print(abc.replace("test","hello")) 
print(abc)


# In[63]:


#split
print(abc.split())


# In[66]:


print(abc.split("e"))


# In[70]:


#Comparison Operator
'''  == ,!=  <> > < '''
a =  5
b= '5'
print(a == b) # false
a === b
#Logical operator and(&&) or(||)


# In[73]:


#Input
age = input("Enter your age")
print("Your age is" + age)


# In[86]:


#Tax calulation
personal_income = int(input("Enter Your personal income "))
tax = int(input("Enter your tax slab "))
amount = personal_income*tax/100
netamount= personal_income - amount
print('Tax amount is:{}'.format(amount))
print('Tax netamount is:{}'.format(netamount))


# In[93]:


amount


# In[113]:


#string oiperation
var = 'Hello world'
print(var[0])
print(var[-1])
print(var[-2])
print(var[:])
print(var[::])
print(var[2:])
print(var[2::3])#upper boundary exclued,lower boundary included
print(var[::5])
print(var[:5])


# In[114]:


var = "Hello World"
var.isupper()


# In[115]:


var.isalpha()


# In[116]:


var.isalnum()


# In[118]:


var.islower()


# In[119]:


#Collection
'''
list --[]
tuples--()
map
dictonary--{}
set
'''


# In[120]:


#list []
x=[1,2,3,"hi"]
x


# In[122]:


y=[1,x]
y


# In[123]:


#access the list element
y[0]


# In[124]:


y[1]


# In[126]:


y[1][0]


# In[127]:


y[1:]


# In[129]:


y[1][1:]


# In[130]:


y[0]='list'


# In[131]:


y


# In[155]:


x.append('add new item')
x


# In[156]:


x.reverse()
x


# In[159]:


x.remove('add new item')
x


# In[166]:


x.sort()


# In[ ]:


#nested list
list1
list2
list2
new_list[list1,list2,list3]


# In[134]:


#Dictonary -key and value {key:value}
dict_ = {1:'test',2:'abc'}
dict_


# In[142]:


dict_.keys()


# In[148]:


y = {'x':[1,2,3]}
y.values()


# In[167]:


#tuples -- immutable
tup1 = (1,2,3,4,5)
tup1[0] = "new"


# In[168]:


max(tup1)


# In[170]:


len(tup1)


# In[171]:


3 in tup1


# In[173]:


#set -- cointains distnt element only
set1 = {1,2,3}
len(set1)


# In[175]:


set1.update({4,5}) # append will not work with set,set element can't be acces perticulr elemnt
set1


# In[176]:


{1,2,2,3,3,3,4,4,4,4,4,4,4,4}


# In[182]:


#control statement 
x = False
if x :
    print("in if")
else:
    print("in else")


# In[186]:


loc = 'Bank'
if loc == 'Auto Shop':
    print ('Welcome to the Auto Shop!')
elif loc == 'Bank':
    print ('Welcome to the bank!')
else:
     print ('Where are you')


# In[194]:


#Tax calulation
personal_income = int(input("Enter Your personal income "))
if(personal_income <= 20000):
    tax = 3
elif (personal_income <= 30000):
    tax = 5
elif (personal_income <= 50000):
    tax = 10
else:
    tax = 20
    
amount = personal_income*tax/100
netamount= personal_income - amount
print('Tax amount is:{}'.format(amount))
print('Tax netamount is:{}'.format(netamount))


# In[196]:


#loops

var =  int(input("Enter the number rage to print"))
for i in range(0,var): 
    print(i)


# In[197]:


#nested loop
list1 = [1,2,3]
for r in list1:
    print(r)


# In[201]:


i = 5
for r in range(0,i):
    print(i*'*')
    i = i-1
    


# In[203]:


#function
def addition(a,b):
    c = a+b
    return c
print(addition(80,9))

