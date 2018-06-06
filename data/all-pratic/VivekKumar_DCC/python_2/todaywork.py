vivek
Last
Checkpoint: 26
minutes
ago
(autosaved)

Logout

Python
3

Trusted
File
Edit
View
Insert
Cell
Kernel
Widgets
Help

Run

The
begining
In[4]:

print('Hello world')
print('vivek')

Hello
world
vivek

Arithmetic
operator
In[5]:

2 + 4

Out[5]:
6

##
In[6]:

2 - 4

Out[6]:
-2
In[7]:

4 - 2

Out[7]:
2
In[8]:

4 * 5

Out[8]:
20
In[9]:

5 / 2

Out[9]:
2.5
In[10]:

5 % 2

Out[10]:
1
In[13]:

5 // 2

Out[13]:
2
In[16]:

5 ** 2

Out[16]:
25
In[21]:

5 + 1 - 4 - (5 ** 7) / 6

Out[21]:
-13018.833333333334
In[18]:

2 ** 10

Out[18]:
1024
In[22]:

6 - (30 / 5)

Out[22]:
0.0

Assignement
operator
with Arithemetic operator
In[23]:

a = 2
​



In[24]:

a + 10

Out[24]:
12
In[25]:

b = 5.0
a + b

Out[25]:
7.0

String
Assignment
In[27]:

c = 'hello'

In[36]:

c

Out[36]:
'hello'
In[34]:

h = "hello"
h

Out[34]:
'hello'
In[35]:

"Hello Let's try this one"

Out[35]:
"Hello Let's try this one"

Income
tax
Calculation
In[43]:

income = 10000
taxpercent = 10
taxableamount = income * (taxpercent / 100)
taxableamount
​


Out[43]:
1000.0

Area
of
circle
In[54]:

r = 5
pie = 3.14
Area = pie * (r ** 2)
Area

Out[54]:
78.5
In[49]:

b = round(20.345, 2)
b

Out[49]:
20.34

How
to
convert
anything
to
integer
In[52]:

Area = int(Area)
Area

Out[52]:
78
In[53]:

Area = float(Area)
Area

Out[53]:
78.0

Multi
line \ is used
to
avoid
appostrpphy
s or single or quote
In[56]:

'''hello
k.jhkjhgklg'''

Out[56]:
'hello\nk.jhkjhgklg'
In[60]:

M = 'I dont\'t like to eat cheese'
print(M)

I
dont
't like to eat cheese

String
concate
In[64]:

a = "Vivek "
b = "Gupta"
c = a + b
print(c)

Vivek
Gupta

HOW
TO
PRINT
FORMATTTED
THINGS
In[66]:

Name = "vivek"
age = 29
print("Myname:{one} and my age is {two}".format(one=Name, two=age))

Myname: vivek and my
age is 29
In[69]:

Name = "Vivek"
age = 29
print("Myname:{} and my age is {}".format(Name, age))
print("Myname:{0} and my age is {1}".format(Name, age))

Myname: Vivek and my
age is 29
Myname: Vivek and my
age is 29
In[77]:

print(3 * "hello ")
print(300 * "hello " + "\n\nThe End")

hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello
hello

The
End
In[78]:

"vivek".upper()

Out[78]:
'VIVEK'
In[79]:

len("hello world")

Out[79]:
11
In[84]:

"Hi  my name is Vivek".replace("Vivek", "Gupta")

Out[84]:
'Hi  my name is Gupta'
In[96]:

bob = "my name is Vivek \n" * 6
bob.replace("Vivek", "vivu")
print(bob)

my
name is Vivek
my
name is Vivek
my
name is Vivek
my
name is Vivek
my
name is Vivek
my
name is Vivek

In[97]:

bob = "my name is Vivek \n" * 5
c = bob.replace("Vivek", "vivu")
print(c)
print(bob)

my
name is vivu
my
name is vivu
my
name is vivu
my
name is vivu
my
name is vivu

my
name is Vivek
my
name is Vivek
my
name is Vivek
my
name is Vivek
my
name is Vivek

In[100]:

bob = "vivek is a nice chap"
bob.split()

Out[100]:
['vivek', 'is', 'a', 'nice', 'chap']
In[103]:

a = 5
b = 1
a > b

Out[103]:
True
In[104]:

a = 5
b = 1
​
a == b

Out[104]:
False
In[107]:

a != b

Out[107]:
True
In[]:

(a == b) or (b < a)

In[3]:

r = input('enter radious value = ')
pie = 3.14
Area = pie * (int(r) ** 2)
print(Area)

enter
radious
value = 5
78.5
In[13]:

employeesalary = input('enter the salary=')
taxslab = input('enter the taxslab=')
taxamount = int(employeesalary) * (int(taxslab) / 100)
netsalary = int(employeesalary) - int(taxamount)
print(netsalary)
print(taxamount)
​
​
​
​
​
​
​
​



enter
the
salary = 100000
enter
the
taxslab = 10
90000
10000.0
In[16]:

var1 = 10
print('here is a number: %s' % (var1))

here is a
number: 10
In[22]:

n = 1
m = 2
print('the sume of %s and %s is equal to %s' % (n, m, n + m))

the
sume
of
1 and 2 is equal
to
3
In[26]:

var = 'helo world'
var[4]
​


Out[26]:
'y'
In[30]:

var = 'helo world'
var[-1]
​


Out[30]:
'd'
In[36]:

var = 'helo world'
var[:2]
​


Out[36]:
'he'
In[37]:

var = 'helo world'
var[2:]

Out[37]:
'lo world'
In[38]:

var = 'helo world'
var[-1]

Out[38]:
'd'
In[45]:

var = 'hello'
print(var[0:5])
print(var[5:0])

hello

In[50]:

var = 'hello'
var.islower()
​


Out[50]:
True
In[51]:

var = 'HELLO'
var.isupper()

Out[51]:
True
In[52]:

var = 'HELLO'
var.isalpha()

Out[52]:
True

# list

In[53]:

z = [1, 2, 3, 4]

In[54]:

x = [1, 2, 3, 'a']

In[68]:

y = [2, x]
print(y)
y[1][3]

[2, [1, 2, 3, 'a']]
Out[68]:
'a'
In[]:


​






# dictionary

In[70]:

d = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(d)

{'Name': 'Zara', 'Age': 7, 'Class': 'First'}
In[80]:

z = {1: 'abc', 2: 'hgf'}
print(z[1])
print(z[2])
b = {1: [1, 2, 3]}
print(b[1][1])

abc
hgf
2
In[84]:

##reverse
newlist = ['a', 'b', 'c', 'd', 'e']
newlist.reverse()
newlist

Out[84]:
['e', 'd', 'c', 'b', 'a']
In[85]:

##sort
a = [4, 7, 1, 9, 2, 3]
a.sort()
a

Out[85]:
[1, 2, 3, 4, 7, 9]
In[89]:

##append
e = [1, 2, 3]
e.append(4)
e
​


Out[89]:
[1, 2, 3, 4]
In[90]:

b = [1, 2, 3]
c = b + [5]
c

Out[90]:
[1, 2, 3, 5]
In[94]:

t = (1, 2, 3, 45)
print(t)
​



(1, 2, 3, 45)
In[95]:

max(t)

Out[95]:
45
In[96]:

45 in t

Out[96]:
True
In[97]:

len(t)

Out[97]:
4
In[99]:

t2 = (1, 2, 3, 5)
t2[1:3]

Out[99]:
(2, 3)
In[]:


​




SET is unorderd
distinct
elements
In[100]:

s = {1, 2, 3}

In[101]:

len(s)

Out[101]:
3
In[102]:

max(s)

Out[102]:
3
In[103]:

min(s)

Out[103]:
1
In[105]:

2 in s

Out[105]:
True
In[106]:

5 in s

Out[106]:
False
In[107]:

s2 = {4, 5}
s.update(s2)
s

Out[107]:
{1, 2, 3, 4, 5}
In[110]:

s3 = {1, 1, 1, 1, 3, 3, 34, 4, 4, 4, 4}
s3
​


Out[110]:
{1, 3, 4, 34}
In[117]:

d = set()
d.add(10)
d

Out[117]:
{10}
In[126]:


​
a = 0
b = 3
​
if (a > b):
    print('a is greater then b')
elif (a == b):
    print('a and b is equal')
elif (b > a):
    print('a smaller too b')

a
smaller
too
b
In[136]:

employeesalary = int(input('enter the salary='))
##taxslab=input('enter the taxslab=')
if (employeesalary >= 10000 and employeesalary <= 20000):
    taxamount = int(employeesalary) * (int(3) / 100)
    netsalary = int(employeesalary) - int(taxamount)
    print('1')
    print(netsalary)
    print(taxamount)
elif (employeesalary >= 20001 and employeesalary <= 30000):
    print('2')
    taxamount = int(employeesalary) * (int(5) / 100)
    netsalary = int(employeesalary) - int(taxamount)
    print(netsalary)
    print(taxamount)
elif (employeesalary >= 30001 and employeesalary <= 40000):
    print('3')
    taxamount = int(employeesalary) * (int(8) / 100)
    netsalary = int(employeesalary) - int(taxamount)
    print(netsalary)
    print(taxamount)

enter
the
salary = 25000
2
23750
1250.0
In[]:


​



