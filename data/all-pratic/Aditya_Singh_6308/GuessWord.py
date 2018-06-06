class GuessWordGame:

    def __init__(self, lifeline=5):
        self.lifeline = lifeline

    @staticmethod
    def getrandomfruit():
        fruits = ["APPLE", "ORANGE", "BANANA", "PINEAPPLE", "GRAPE", "MANGO", "KIWI", "GUAVA", "MELON"]
        #word = fruits[np.random.randint(0, 8)]
        return fruits[0]

    def decreaselifeline(self):
        if self.lifeline == 0:
            return False
        else:
            self.lifeline = self.lifeline - 1
            return True


game = GuessWordGame()
fruit = game.getrandomfruit()
print(fruit)
length = len(fruit)
print("You have to guess a word of length - ", length)
i = 0
answer = ""
inp = ""
userinput = ""
while i <= length:
    if len(answer) > 0:
        inp = "Your Input : " + answer + "."

    userinput = input(inp + "You have " + str(game.lifeline) + " lifeline left. Enter next character : ")
    if fruit[i] == userinput:
        i = i + 1
        answer = answer + userinput
        print("You have guessed it right")
    else:
        print("Your input is wrong. Please try again")
        if game.decreaselifeline():
            continue
        else:
            print("You don't have any life left. Thank you for trying")
            break
    if answer == fruit:
        print("You win")
        break


