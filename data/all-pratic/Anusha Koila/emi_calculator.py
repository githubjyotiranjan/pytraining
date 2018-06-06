#Input : LOAN AMOUNT, RATE OF INTEREST , LOAN PERIOD
#CALCULATE SIMPLE INTEREST, TOTAL PAYABLE AMOUNT

loan_amt=input("Enter Loan Amount you need :")
loan_period=input("Enter period you want to pay the loan :")
rate_interest=input("Enter rate of interest :")

loan_amt=int(loan_amt)
loan_period=int(loan_period)
rate_interest=int(rate_interest)

SI=(loan_amt*rate_interest*loan_period)/100

Total_amt=loan_amt+SI

EMI=Total_amt/loan_period

print("Total Payable Amount is : %s"%(Total_amt))
print("EMI per year is : %s"%(EMI))
print("EMI per month is : %s"%(EMI/12))

CI=loan_amt*((1+(rate_interest/100))**loan_period)

print("Compound interest : %s"%(CI))