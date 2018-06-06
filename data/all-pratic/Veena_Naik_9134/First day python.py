
# coding: utf-8

# In[1]:


g=9


# In[2]:


g


# In[3]:


age=input("enter your age")


# In[7]:


pi=3.14
radius=int(input("enter your radius"))
area=pi*radius*2
print(area)


# In[9]:


netincome=int(input("enter your salary"))
tax=(netincome*10)/100
print("netincome:"+netincome)
print("tax"+tax)


# In[21]:


salary=int(input("enter your salary"))
tax=(salary*10)/100
print('tax={}'.format(tax))
Netincome=salary-tax
print('Netincome:{}'.format(Netincome))


# In[22]:


s='my name is abc'
print(%s)


# In[32]:


a=15451
print("here %f"%(a))


# In[34]:


a=19
b=1
print('the addition of %s and %s is %s'%(a,b,a+b))


# In[41]:


a=1
print('addition %s'%a)


# array working

# In[46]:


a="hello world"
print(a[-1])


# In[61]:


b="helloworld"
print(b[5:])


# In[67]:


b.count("l")


# In[70]:


b.capitalize()


# In[71]:


b.find(e)


# In[72]:


b.find('e')


# In[73]:


b.expandtabs()


# In[74]:


b.format()


# In[77]:


list= {1,2,'hi'}


# In[78]:


list


# In[79]:


b=[list,1]


# In[80]:


b


# In[81]:


list[1]


# In[82]:


b[1]


# In[83]:


b[0]


# In[84]:


b[:2]


# In[85]:


b[2:]


# In[88]:


b[1]=6


# In[89]:


b


# In[92]:


b[1][0]


# In[95]:


D1={1:"key",2:"name"}


# D1

# In[98]:


D1[2][1]


# In[101]:


D1={1:"key",4:"name"}


# In[103]:


D1[4][2]


# In[104]:


list


# In[105]:


b


# In[108]:


b=b+['hi']


# In[109]:


b


# In[110]:


b.pop(0)


# In[111]:


b.append('hello')


# In[112]:


b


# In[113]:


b.reverse()


# In[114]:


b


# In[115]:


b.sort()


# In[116]:


b[2]


# In[117]:


b[2]='6'


# In[118]:


b


# In[119]:


b.sort()


# In[120]:


b


# In[122]:


b.insert(3,'bye')


# In[123]:


b


# In[124]:


tup1=(2,1,3,4)


# In[125]:


tup1


# In[128]:


tup1[2]=9


# In[129]:


tup1


# In[130]:


max(tup1)


# In[131]:


tup2=(3,6,7)


# In[132]:


tup3=tup1+tup2


# In[133]:


tup3


# In[134]:


6 in tup3


# In[135]:


set1={1,2,3,1,4,5,1}


# In[136]:


set1


# In[137]:


set2={9,8}


# In[138]:


set2


# In[139]:


set1.update(set2)


# In[140]:


set1


# In[141]:


v=set()


# In[142]:


v.add(3)


# In[143]:


v


# In[144]:


v.insert(2)


# In[146]:


v.intersection()


# In[162]:


if 1>2: 
    print("hi") 
elif 3<4:
    print("hello")
else: 
    print("bye")


# In[180]:


salary=int(input("enter your salary"))
if 10000<salary<=20000:
    tax=(salary*3)/100
elif 21000<salary<30000:
    tax=(salary*5)/100 
elif 31000<salary<50000:
    tax=(salary*10)/100 
else:
    tax=(salary*20)/100 
print("Tax paid={}".format(tax)) 
print("NetIncome={}".format(salary-tax))
    


# In[174]:


tax


# In[175]:


salary

