word_input="Apple"
word_length=len(word_input)
word_input=word_input.lower()
letter_guess = ''
count = 0
limit = 10
livesleft=limit
correct_words=0


while livesleft >= 1:
    letter_guess = input('Guess a letter: ')
    letter_guess=letter_guess.lower()

    if letter_guess in word_input:
        print(' It is correct')
        count += 1
        correct_words +=1

    if letter_guess not in word_input:

        livesleft -=1
        if livesleft==0:
         print("Sorry .Left with No Chances!!!")
        else:
         print('Wrong Answer!Left with {}'.format(livesleft))
        count += 1
    if correct_words==word_length:
        print("You have guessed all the letters correctly")
        break


