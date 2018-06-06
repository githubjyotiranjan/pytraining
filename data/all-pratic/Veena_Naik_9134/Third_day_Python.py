
# coding: utf-8

# In[ ]:


import random

word = ('apple')

correct = word

letter_guess = ''
word_guess = ''
store_letter = ''
count = 0
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')
print('\n')

while count < limit:
    letter_guess = input('Guess a letter: ')

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess
        count += 1

    if letter_guess not in word:
        print('no!')
        count += 1

   

print('\n')
print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')
while word_guess:
    if word_guess.lower() == correct:
        print('Congrats!')
        break

    elif word_guess.lower() != correct:
        print('Unlucky! The answer was,', word)
        break

print('\n')
input('Press Enter to leave the program')


# In[2]:


import numpy as np


# In[3]:


np.zeros(10)


# In[5]:


np.ones(3)*5


# In[12]:


x=np.arange(10,51,2)


# In[14]:


np.array(x)


# In[20]:


np.arange(9).reshape(3,3)


# In[16]:





# In[17]:


a=[[0,1,2],[3,4,5]]


# In[18]:


np.array(a)


# In[21]:


np.eye(3)


# In[34]:


np.random.randn(25)


# In[36]:


np.arange(1,101).reshape(10,10)/100


# In[46]:


np.linspace(0,1,4)


# In[70]:


a=np.arange(12,26)
np.delete(a,[4,9]).reshape(3,4)


# In[56]:


s=np.arange(1,26).reshape(5,5)


# In[60]:


s[:2,2:]


# In[57]:


np.arange(1,26).reshape(5,5)


# In[79]:


a=np.arange(2,13,5).reshape(3,1)


# In[80]:


a


# In[81]:


s=np.arange(1,26).reshape(5,5)


# In[89]:


sum(s)


# In[92]:


f=np.arange(21,26)


# In[93]:


sum(f)


# In[100]:


s.sum(1)


# In[101]:


f


# In[102]:


s


# In[103]:


sum(s)


# In[108]:


s.sum(1)


# In[109]:


d={'a':1,'b':2,'c':3}


# In[110]:


d


# In[111]:


d.key


# In[116]:


d.keys()


# In[117]:


import pandas as pd


# In[128]:


pd.Series(data=d)


# In[126]:


s


# In[142]:


pd.Series(f,lab)


# In[139]:


lab=['a',1,2,3,4]


# In[144]:


s1=pd.Series([1,2],index=['hi','bye'])


# In[145]:


s2=pd.Series([1,2],index=['hi','lie'])


# In[146]:


s1+s2


# In[148]:


s1['hi']

