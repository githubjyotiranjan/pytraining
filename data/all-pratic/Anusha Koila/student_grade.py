#Student Grading

name=input("Enter name of student :")
mark=input("Enter mark of an student :")
mark=int(mark)
if(mark>=90 and mark<=100):
    grade='A+'
elif(mark>=80 and mark<90):
    grade = 'A'
elif(mark>=70 and mark<80):
    grade = 'B'
elif(mark>=60 and mark<70):
    grade = 'C'
else:
    grade='FAIL'

print("Name of the student : %s"%(name))
print("Marks  :%s "%(mark))
print("Grade  :%s "%(grade))
