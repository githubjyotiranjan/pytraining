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