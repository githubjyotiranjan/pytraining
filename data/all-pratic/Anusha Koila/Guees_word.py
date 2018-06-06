##GUESS THE WORD

Word="ANUSHA"

list=['A','N','U','S','H','A']
a=10
print("---- Guess the word ---")
print("You have %s attempts left"%(a))

word_len=len(list)
i=0
while(i!=word_len and a>0):
    w1=input("Enter the %s letter :"%(i+1))
    w1=w1.upper()
    if(list[i]==w1):
        print("You got it right..!!!")
        i=i+1
    else:
        print("Wrong... Try again")
        a=a-1
        print("You are left with %s attempts"%(a))
        continue;
if(a>0):
    print(" **  CONGRATULATIONS ** ")
else:
    print("Sorry... You lost the game ")


