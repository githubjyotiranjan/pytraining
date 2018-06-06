
'''EMI by Simple Interest'''
LoanAmount=int(input("Enter the Loan Amount"))
InterestRate=int(input("Enter the Interest Rate"))
Duration=int(input("Enter the duration of your loan in years"))
SimpleInterest=(LoanAmount*InterestRate*Duration)/100
TotalAmountSI=LoanAmount+SimpleInterest
EMISI=TotalAmountSI/Duration
print('Interest is{}'.format(SimpleInterest))
print('Total Amount  is{}'.format(TotalAmountSI))
print('EMI  is{}'.format(EMISI))


TotalAmountCI=LoanAmount*(1+InterestRate/100)**Duration

EMICI=TotalAmountCI/Duration

print('Total Amount  is{}'.format(TotalAmountCI))
print('EMI  is{}'.format(EMICI))
