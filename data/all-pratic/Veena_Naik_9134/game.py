print("\t\tWelcome to Word Guess game!")
print("You have 5 attempts to guess the word that I have choosen.",

      "\nI can only reply with 'yes' or 'no' and tell you the length of the word!\n")

WORD = ('Python')

correct = WORD

tries = 1

hint = WORD[0]

# Tell the player the length of the word and let them guess it for the first time

print("\t\tLength of the word: ", len(WORD), "\n")

guess = input("Guess the letter: ")

# Guessing loop

while guess.lower() != correct.lower() and guess != "" and tries <= 5:

    print("No!")

    tries += 1

    if tries == 3:

        response = input("Would you like a hint? y or n: ")

        if response.lower() == "y":
            print("The first letter of the word is: ", hint)

    print("\nTries remaining: ", 6 - tries)

    guess = input("Guess the word: ")

# Tell the player they was right or ran out of tries

if guess.lower() == correct.lower():
    print("\nYes! You guessed the word! The word was: ", correct)

    print("You guessed it in ", tries)