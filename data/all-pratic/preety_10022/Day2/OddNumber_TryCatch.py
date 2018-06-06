try:
 a = int(input("Enter a positive number"))
 if(a<0):
  raise ValueError("Enter a valid Number")
except ValueError as ve:
 print(ve)

for i in range(0,a):
   if(i%2!=0):
     print(i)


