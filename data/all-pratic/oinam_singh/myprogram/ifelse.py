sal=float(input("Enter salary "))
if sal>=1000000:
    print ("Tax more than1000000")
    tax=30/100
elif sal>=500000:
    print("Tax more than 500000 but less than 1000000" )
    tax = 20 / 100
else:
    print("Tax less than 500000")
    tax = 10 / 100
taxAmount = sal * tax;
print("Net tax for salary %.2f is %.2f" % (sal, taxAmount))