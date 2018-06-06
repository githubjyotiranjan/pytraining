ReceivedMarks=int (input("Enter the Received Marks: "))
if 500>ReceivedMarks>400:
 Grade="A"
elif 400>ReceivedMarks>300:
 Grade = "B"
elif 30000>ReceivedMarks>20000:
 Grade = "C"
else:
 Grade = "D"

print('Student received marks is {} and Grade is {}'.format(ReceivedMarks,Grade))