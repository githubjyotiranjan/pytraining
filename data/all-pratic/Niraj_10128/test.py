loanAmount = int(input('enter the loan amount'))
roi = int(input('enter the rate of interest'))
time = int(input('enter the loan period'))/12

interest = (loanAmount*roi*time)/100
amount = loanAmount+interest


print('your emi is :',amount)

ci = loanAmount*(1+interest/100)**time
print(ci)
