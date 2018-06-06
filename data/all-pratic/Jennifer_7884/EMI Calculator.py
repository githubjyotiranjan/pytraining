principal=float(input("Enter the loan amount: "))
rate=float(input("Enter the rate of interest: "))
period=float(input("Enter the loan period: "))

si = principal * rate * period / 100
total = principal+si
emi = total/period
ci = principal * ((1+(rate/100))**(period/12))
print("Total payable : %s" %total)
print("EMI : %s" %emi)
print("Compound interest : %s" %ci)
