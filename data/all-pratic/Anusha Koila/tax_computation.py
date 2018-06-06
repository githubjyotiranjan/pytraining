#Tax Computation
# 10k -20k --> 3%
#21 -30k --> 5%
#31 - 50k --> 10%
# >51k  --> 20%

salary=input("Enter Salary of an employee :")
salary=int(salary)
if(salary>=10000 and salary<=20000):
    tax=int(salary)*(3/100)
elif(salary>20000 and salary<=30000):
    tax=int(salary)*(5/100)
elif(salary>30000 and salary<=50000):
    tax=int(salary)*(10/100)
else:
    tax=int(salary)*(20/100)

net=salary-tax
print("Total Payable tax : %s"%(tax))
print("Net Income :%s "%(net))
