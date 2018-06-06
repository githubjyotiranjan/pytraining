Loan_amount=int(input("enter loan amount"))
RI=int(input("enter rate of interest"))
Time=int(input("enter period"))
CI=Loan_amount*((1+(RI/100))**Time)
Total_Payable_amount=CI+Loan_amount
EMI=(Total_Payable_amount)/Time
print("EMI{}".format(EMI))