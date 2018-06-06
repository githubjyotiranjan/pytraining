marks = float(input("Enter Marks: "))
if marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80 and marks <= 89:
    grade = "A"
elif marks >= 70 and marks <= 79:
    grade = "B"
elif marks >= 60 and marks <= 69:
    grade = "C"
else:
    grade = "Fail"
print("My grade is %s" % (grade))