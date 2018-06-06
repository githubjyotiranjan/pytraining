LoanAmount = int(input("Please enter your loan amount"))
ROI = int(input("Please enter ROI"))
Duration = int(input("Please enter Duration in months"))

SimpleInterest: int = LoanAmount*ROI*Duration / 100

CompundImterest : int = LoanAmount* (1 + ROI/100)** Duration
TotalAmount: int = LoanAmount + SimpleInterest

TotalAmountwithCP: int = LoanAmount + CompundImterest

EMI: int = TotalAmount/Duration

print("Total Amount is {}".format(TotalAmount))
print("Total Amount with compound interest is {}".format(TotalAmountwithCP))
print("EMI is {}".format(EMI))
