taxSlab = {3:[10000,20000], 5:[20001,30000], 10:[30001,50000],20:[50001]}
taxSlab.get
salary=int(input("Enter your salary: "))


if salary > taxSlab.get(3)[0] and salary < taxSlab.get(3)[1]:
    tax=salary*3/100
elif salary > taxSlab.get(5)[0] and salary < taxSlab.get(5)[1]:
    tax=salary*5/100
elif salary > taxSlab.get(10)[0] and salary < taxSlab.get(10)[1]:
    tax=salary*10/100
else:
    tax=salary*20/100
netSalary=salary - tax
print("Your net salary is: ", netSalary)
print("Your tax liability is: ", tax)

