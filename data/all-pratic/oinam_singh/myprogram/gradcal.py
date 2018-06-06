mark=float(input("Enter mark : "))
if mark>100:
    grad='Invalid mark'
elif mark>=90 and mark<=100:
    grad='A'
elif mark>=80 and mark<90:
   grad='B'
elif mark>=70 and mark<80:
   grad='C'
elif mark>=60 and mark<70:
   grad='D'
else:
    grad='F'
print("Student grad for mark %d is %s" % (mark, grad))