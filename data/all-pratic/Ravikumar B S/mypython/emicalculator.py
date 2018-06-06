loanamt = float(input("Enter Loan Amount: "))
intrate = float(input("Enter Interest Rate: "))
loanper = float(input("Enter Loan Period in Years: "))

intamt = loanamt * intrate * loanper / 100
totalamt = loanamt + intamt
emiamt = totalamt/(loanper * 12)

print("\n Simple Interest - Starts")
print("your loan amount is %1.2f" % (loanamt))
print("Total interest payable for %d years is %1.2f" % (loanper,intamt))
print("EMI is %1.2f" % (emiamt))
print("Simple Interest - Ends\n")

print("\n Compount Interest - Starts")
cintamt = loanamt * (((1 + intrate)**loanper) - 1)
ctotalamt = loanamt + cintamt
cemiamt = ctotalamt/(loanper * 12)
print("your loan amount is %1.2f" % (loanamt))
print("Total interest payable for %d years is %1.2f" % (loanper,cintamt))
print("EMI is %1.2f" % (cemiamt))
print("Compound Interest - Ends\n")