# salary = int(input("Enter your salary"))
# if 10000 <= salary < 20000:
#     tax_slab = 3
# elif 20000 <= salary < 30000:
#     tax_slab = 5
# elif 30000 <= salary < 50000:
#     tax_slab = 10
# else:
#     tax_slab = 20
# tax = salary * tax_slab/100
# print("tax is {}".format(tax))
# print("net salary is {}".format(salary - tax))
#
#


# marks = int(input("Enter your marks"))
#
# if 90 <= marks < 100:
#     print("A plus")
# else:
#     print("F grade")



# EMI Calculator
#
# i/p:
# loan amount
#  rate of interest
# load period
# SI = simple interest
# total payable amount = loan amount + interest
#
# EMI = total payment amount / load period
# compound interest


loan_amount = int(input("Enter the load amount"))
roi = int(input("Enter the rate of interest"))
loan_period = int(input("Enter the load period in years"))

# si = (loan_amount*roi*loan_period) / 100
# total_amt = si + loan_amount

ci =(roi/100)**loan_period
total_amt = loan_amount * (1 + ci)

# print("Simple Interest is {}".format(si))
print("total amount payable is {}".format(total_amt))
print("EMI is {}".format(total_amt/loan_period))

