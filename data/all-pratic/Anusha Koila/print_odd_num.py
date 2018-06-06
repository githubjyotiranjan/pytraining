#print odd numbers
#raise exception when negtive numbers are inputted

try:
    num = int(input("Enter an number :"))
except erro1:
    if(num<0):
        print("Negative numbers not allowed")
else:
    print("ODD numbers list :\n ")
    for i in range(1,num):
        res=i%2
        if(res!=0):
            print(i)
            i=i+1

