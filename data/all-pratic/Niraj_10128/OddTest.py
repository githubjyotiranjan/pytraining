"""
num = input("Enter the number")

try:
    num = int(num)
    if num%2==0 :
        num=num-1

    while num>0:
        print(num)
        num=num-2

except:
    print("Input is wrong")

"""

#lamda function
sum = lambda num1, num2: num1+num2
print('The value of 10 and 20 is', sum(10,20))