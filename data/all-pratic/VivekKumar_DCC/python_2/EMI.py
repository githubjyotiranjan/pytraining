loanamount=int(input('enter the marks in loanamount='))
rateofinterest=int(input('enter the marks in rateofinterest='))
loanperoid=int(input('enter the marks in loanperoid='))
simpleinterest=(loanamount*rateofinterest*loanperoid)/100
print('simpleinterest ='+str(simpleinterest))
TPA=loanamount+simpleinterest
print('TPA ='+str(TPA))
EMI=TPA/loanperoid
print('EMI ='+str(EMI))
compundint=int(loanamount)*(1+int(rateofinterest)**int(loanperoid))
print('compundint ='+str(compundint))



