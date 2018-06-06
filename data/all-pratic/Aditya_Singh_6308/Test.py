
# coding: utf-8

# In[1]:

"""
print("Hello Adi")


# Intro

# In[10]:


num = 20
print(num)
num = num + 2
print(num)
num = num * 2
print(num)
num = num - 2
print(num)
num = num / 2
print(num ," - ")
num = num // 2
print(num)
num = num % 4
print(num)
num = num ** 2
print(num)


# In[22]:


num = 20 / (5 + 5) * 5 - 5 % 2
print(num)


# In[23]:


print(num)


# In[25]:


print(num < 1)


# In[26]:


print(5666666666666666666666666666666666.0000000000000023444444)


# In[27]:


print(1232133333333333333333333333333333333333333333333333333333333333333333)


# In[28]:


num = 12333333333333333333333333333335332 + 243238597320590304845324235335
print(num)


# In[30]:


num = 'It was a number'
print(num)


# 'Hello' "World"

# In[33]:


num = "Hell'o World" "It's new"
print(num)


# Print Tax Amount Of A Person

# In[40]:


name = "John"
salary = 100000
tax = 10
print(name, "has to pay tax of Rs.",(salary*10)/100)


# In[48]:


pi = 3.14
radius = 5.5
area = pi * radius**2
print(area)


# Round()

# In[51]:


print(round(area, 2))


# In[52]:


int(area)


# In[53]:


float(area)


# In[54]:




# In[56]:





# Escaping

# In[66]:


mystery='I Don\'t like to eat cheese'
print(mystery)
mystery="I Don't like to eat cheese"
print(mystery)
mystery="I Don't like to eat \"cheese\""
print(mystery)


# String Concatenation & Formatting

# In[78]:


firstName = "John"
lastName = "May"
fullName = firstName + " " + lastName
print({fullName})
print("My first name is {firstName} and last name is {lastName}".format(firstName=firstName,lastName=lastName))
print("My first name is {} and last name is {}".format(firstName,lastName))
print("My first name is", {firstName}, "and last name is ", {lastName})
print("My first name is", firstName, "and last name is ", lastName)


# In[95]:


print(3 * "Hello \n")
print("Hello " * 3)


# String Functions

# In[115]:


print(fullName.capitalize())
print(fullName.upper())
print(fullName.replace('Mayor', 'mayer'))
print(fullName.lower())
len(fullName)
fullName.split(' ')
print(fullName.count('M'))
print(fullName.find('M'))
print(fullName.index('M'))
print(fullName.istitle())


# In[118]:


firstName > lastName


# In[119]:


# In[120]:


5 and 5


# In[121]:


True and False


# In[122]:


True or False


# In[124]:


True or False and True


# In[127]:


False or True and False


# In[135]:


pi = 3.14
radius = input("Enter the radius : ")
area = pi * int(radius)**2
print(area)
radius = input("Enter the radius : ")
area = pi * int(radius)**2
print(area)
radius = input("Enter the radius : ")
area = pi * int(radius)**2
print(area)


# In[137]:


firstName[1:3]


# Ask Salary of an employee and ask the task slab & print the net salary as well as tax amount

# In[140]:


salary = int(input("What is ur salary : "))
taxSlab = int(input("Which tax slab you belong : 10, 20, 30 : "))
taxAmt = (salary * taxSlab)/100
netSalary = salary - taxAmt
print("taxAmt - ", taxAmt, ", Net Salary : ", netSalary)


# In[142]:


9**(1/2)


# In[171]:


print('Hello %d' %netSalary)


# In[172]:


firstName[-1]


# In[186]:


n = -1*len(firstName)
firstName[1:]


# In[192]:


firstName.endswith('n')


# Collaction

# In[207]:


numbers = [[1,2,3],[5,6,7],[1]]
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[1][1])
print(numbers[1:])


# In[223]:


dictionary = {"Fruits" : ["Apple","Orange","Banana"], "Drinks":["Coca"]}
print(dictionary)
print(dictionary.items())


# In[222]:


print(dictionary.get('Fruits')[2])


# In[218]:


print(dictionary.get(1))


# In[226]:


numbers + ["Veg"]


# In[235]:


dictionary.update({"Veg":"Potato"})


# In[228]:


print(dictionary)


# In[242]:


dictionary.popitem()


# In[243]:


print(dictionary)


# In[6]:


txt = [1,2,3,0]
txt1 = txt.copy()
txt.reverse()
txt[1] = 5
print(txt)
print(txt1)


# In[256]:


test1 = {1:'a',2:'b'}
test2 = test1.copy()
test2.update({1:'c'})
print(test2)
print(test1)


# In[7]:


if txt[0]>0:
    print(txt[0])


# In[262]:


tuple = (1,2,3,4,5)
tuple[0]


# In[268]:


tuple[1:]


# In[264]:


max(tuple)


# In[265]:


sum(tuple)


# In[267]:


print(tuple[1] is str)


# In[271]:


a = None
print(a)


# In[295]:


set1 = {71, 2, 3, 4, 1, 2, 3, 4, 5}
set2 = set1
set2.add(6)
set2.issubset(set1)
set2.discard(1)
set3 = {10,20}
set2.union(set3)


# In[4]:


s = set()


# In[11]:


x = 4
if x==1:
    print(x)
elif x==2:
    print(x)
else:
    if x==3:
        print(x)
    else:
        print(x)


# In[24]:


salary = int(input("Enter ur salary : "))
if salary >= 10000 and salary <= 20000:
    tax = 3
elif salary >= 21000 and salary <= 30000:
    tax = 5
elif salary >= 31000 and salary <= 50000:
    tax = 10
else:
    tax = 20
print(tax)
taxAmount = (salary*tax)/100
netAmount = salary - taxAmount

print("Net Salary : ", netAmount, " and total tax : ", taxAmount)


# Student Grading

marks = int(input("Enter ur marks : "))
if marks >= 90 and marks <= 100:
    grade = 'A+'
elif marks >= 80 and marks <= 89:
    grade = 'A'
elif marks >= 70 and marks <= 79:
    grade = 'c'
elif marks >= 60 and marks <= 69:
    grade = 'c'
else:
    grade = 'Fail'
print(grade)


#SI and CI
loanAmt = float(input("Enter loan amt : "))
roi = float(input("Enter roi : "))
loanPeriod = int(input("Enter the tenure of loan in months"))
si = loanAmt * roi * loanPeriod / 100
totalPayableAmt = loanAmt + si
emi = totalPayableAmt/loanPeriod
print("Total Payable amount : ", totalPayableAmt)
print("Emi : ", emi)
ci = loanAmt*(1+roi/100)**loanPeriod
emi = ci/loanPeriod
print("Total Payable amount : ", round(ci, 2))
print("Emi : ", emi)

# For loop

for i in range(0, 5):
    print(i)

list1 = [5,6,7]
for i in list1:
    print(i)
var = 5
# While loop
while var >= 0:
    print('*' * var)
    var = var - 1

# Add


def addition(a, b):
    return a+b


add = addition(3, 4)
print(add)


# Try Catch
try:
    number = int(input("Enter a number: "))
    if number < 0:
        number = input("Enter a +ve number: ")
except ValueError as error:
    print(error)

# lmabda function

sum1 = lambda a, b: a+b
print(sum1(10, 20))



class Main:
    import Importing
    test1 = Importing.Test(50, 60)
    test1.c = 30
    print(test1.add())

"""
# File reading and writing

# file = open("TestFile.txt", "w")
# file.write("Hello\nTest")
file = open("TestFile.txt", "r")
listOfWord = file.read().replace('\n', ' ').split(' ')

count = 0
keyDict = {}
for word in listOfWord:
    if keyDict.get(word) is None:
        keyDict.update({word: 1})
    else:
        count = int(keyDict.get(word))
        keyDict.update({word: (count+1)})
        count = 0
keySet = keyDict.keys()
keyList = []
for word in keySet:
    keyList.append(word)
keyList.sort()
file = open("WordFile.txt", "w")
for word in keyList:
    text = word + " - " + str(keyDict.get(word)) + "\n"
    file.write(text)








