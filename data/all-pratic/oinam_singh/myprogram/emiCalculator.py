p=float(input("Enter loan amount : "))
r=float(input("Enter loan rate : "))
t=float(input("Enter loan duration : "))

i=p*r*t/100
amount=p+i
print("Loan interest for the principal %.2f is %.2f" % (p, i))
print("Loan amount after %d year is %.2f" % (t,amount))

print ("Using compound interest ")
amount=p*(1+r/100)**t
print("Loan amount after %d year is %.2f" % (t,amount))
emi=amount/t
print("EMI per year is %.2f" %emi)
