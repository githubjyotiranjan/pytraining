employeesalary=int(input('enter the salary='))
##taxslab=input('enter the taxslab=')
if(employeesalary >= 10000 and employeesalary <=20000):
 taxamount=int(employeesalary)*(int(3)/100)
 netsalary=int(employeesalary)-int(taxamount)
 print('1')
 print(netsalary)
 print(taxamount)
elif(employeesalary >= 20001 and employeesalary <=30000):
 print('2')
 taxamount=int(employeesalary)*(int(5)/100)
 netsalary=int(employeesalary)-int(taxamount)
 print(netsalary)
 print(taxamount)
elif(employeesalary >= 30001 and employeesalary <=40000):
 print('3')
 taxamount=int(employeesalary)*(int(8)/100)
 netsalary=int(employeesalary)-int(taxamount)
 print(netsalary)
 print(taxamount)