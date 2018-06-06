sal = float(input("Enter Salary: "))
if sal >= 10000 and sal <= 20000:
    taxper = 3
elif sal >= 21000 and sal <= 30000:
    taxper = 5
elif sal >= 31000 and sal <= 50000:
    taxper = 10
else:
    taxper = 20
tax = sal * taxper / 100
nsal = sal - tax
print("Net salary is %1.2f" % (nsal))

