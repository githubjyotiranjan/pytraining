
marks=int(input("Enter marks: "))
if marks >= 90 and marks <= 100:
    print('A+')
elif marks >= 80 and marks <= 89:
    print('A')
elif marks >= 70 and marks <= 79:
    print('B')
elif marks >= 60 and marks <= 69:
    print('C')
else:
    print('Fail')