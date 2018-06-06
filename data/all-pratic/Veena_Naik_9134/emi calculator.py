Loan_amount=int(input("enter loan amount"))
RI=int(input("enter rate of interest"))
Time=int(input("enter period"))
SI=(Loan_amount*RI*Time)/100
Total_Payable_amount=SI+Loan_amount
EMI=(Total_Payable_amount)/Time
print("EMI{}".format(EMI))