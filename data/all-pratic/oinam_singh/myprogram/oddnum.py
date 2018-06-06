val=int(input("Enter a number "))
try:
   if val<0 :
       raise Exception ('Only positive integer')
except Exception as e:
    print("Please enter ",e.args,val)
else:
    for i in range(1,val):
        if i%2:
            print(i, end =' ')
