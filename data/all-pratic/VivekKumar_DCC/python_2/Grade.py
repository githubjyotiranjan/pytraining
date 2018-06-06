maths=int(input('enter the marks in maths='))
science=int(input('enter the marks in science='))
English=int(input('enter the marks in English='))
Geography=int(input('enter the marks in Geography='))
History=int(input('enter the marks in Geography='))
##taxslab=input('enter the taxslab=')
grade=((maths+science+English+Geography+History)/5)*100
if(grade>= 90):
    print('A+')
elif(grade<=80):
 print('b')
elif(grade<=70):
 print('c')