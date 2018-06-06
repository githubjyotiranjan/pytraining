
# coding: utf-8

# Loan 

# In[1]:


LoanAmount = int(input("Please enter your loan amount"))
ROI = int(input("Please enter ROI"))
Duration = int(input("Please enter Duration in months"))

SimpleInterest: int = LoanAmount*ROI*Duration / 100

CompundImterest : int = LoanAmount* (1 + ROI/100)** Duration
TotalAmount: int = LoanAmount + SimpleInterest

TotalAmountwithCP: int = LoanAmount + CompundImterest

EMI: int = TotalAmount/Duration

print("Total Amount is {}".format(TotalAmount))
print("Total Amount with compound interest is {}".format(TotalAmountwithCP))
print("EMI is {}".format(EMI))


# In[4]:


var = int(input("print the numbers upto" ))
for i in range(0,var):
    print(i)


# In[14]:


var = int(input("enter the number of stars you want to print"))

while var > 0:
    print('*' * var )
    var = var - 1


# In[19]:


LoanAmount = int(input("Please enter your loan amount"))
ROI = int(input("Please enter ROI"))
Duration = int(input("Please enter Duration in months"))

def CalculateInterest(amount,interest,duration,Type):
    if(Type == "Simple"):
        return LoanAmount*ROI*Duration / 100
    else: 
        return LoanAmount* (1 + ROI/100)** Duration

SimpleInterest: int = CalculateInterest(LoanAmount,ROI,Duration,"Simple")

CompundImterest : int = CalculateInterest(LoanAmount,ROI,Duration,"Compound")
TotalAmount: int = LoanAmount + SimpleInterest

TotalAmountwithCP: int = LoanAmount + CompundImterest

EMI: int = TotalAmount/Duration

print("Total Amount is {}".format(TotalAmount))
print("Total Amount with compound interest is {}".format(TotalAmountwithCP))
print("EMI is {}".format(EMI))

