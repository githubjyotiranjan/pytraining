import numpy as np

secretWords = ["rose", "thorn", "flower", "plant", "grow", "beautiful"]
secret = secretWords[np.ra]
lives = 10
wordList = ['*', '*', '*', '*']

def checkWordMatch(secret, word, lives, wordList):
    valid = True

    for i in range(0, len(word)):
        if word[i] != secret[i]:
            wordList[i] = '*'
            valid = False
        else:
            wordList[i] = word[i]

    if valid == False:
        lives = lives - 1
        inputString = "Lives : %s " % lives + "You entered %s! Try again! " %''.join(wordList)
        match(secret, lives, inputString)

    return valid


def match(secret, lives, inputString):
    if lives != 0:
        word = input(inputString)

        if len(word) != 4:
            lives = lives - 1
            inputString = "Lives : %s" %lives + " You haven't entered a 4 letter word! Try again! "
            match(secret, lives, inputString)
        elif word.isalpha() == False:
            lives = lives - 1
            inputString = "Lives : %s" %lives + " Your word must contain only letters! Try again! "
            match(secret, lives, inputString)
        elif checkWordMatch(secret, word, lives, wordList) == True:
            print("Good job!! You Won!!!")
            exit(1)
    else :
        print("Aww! Game over!!!")
        exit(1)


inputString = "Lives : %s" % lives + " Enter a four letter word: "
match(secret, lives, inputString)





