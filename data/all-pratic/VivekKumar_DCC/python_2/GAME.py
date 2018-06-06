print("Guess a five letter fruit name")
vals = 0;
for attempt in [1,2,3,4,5,6,7,8,9,10]:
    print("This is your "+str(attempt)+" attempt")
 #   while (vals <= attempt):
   #     vals = vals + 1;
    letter1=input('enter the first letter=')
    if letter1.lower()=='a':
      print("Great going to have the 1st letter")
    else:
        print("Incorrect guess start once again")
        continue
    letter2 = input('enter the letter2=')
    if letter2.lower()=='p':
        print("Great going to have the 2nd letter")
    else:
        print("Incorrect 2nd guess start once again")
        continue
    letter3 = input('enter the letter3=')
    if letter3.lower()=='p':
        print("Great going to have the 3rd letter")
    else:
        print("Incorrect 3rd guess start once again")
        continue
    letter4 = input('enter the  letter4=')
    if letter4.lower()=='l':
        print("Great going to have the 4th letter")
    else:
        print("Incorrect 4th guess start once again")
        continue
    letter5 = input('enter the letter5=')
    if letter5.lower()=='e':
        print("Great going to have the 5th letter")
        print("You won")
        exit(0)
    else:
        print("Incorrect 5th guess start once again")
        break
