class Hangman:
    def __init__(self):
        print("Welcome User. Ready to guess !! I hope its your lucky day")
        print("(1)Yes.I'll Play \n(2)No, Exit")
        user_choice_1 = input("->")

        if user_choice_1 == '1':
            self.start_game()
        elif user_choice_1 == '2':
            exit()
        else:
            print("Invalid Request. Enter again")
            self.__init__()

    def start_game(self):
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = "pikku"
        progress = ["?", "?", "?", "?", "?"]

        while guesses < 6:
            guessed_word = "".join(progress)
            if guessed_word == the_word:
                print("Successfully done! \n\n\n")
                var = input("Wanna continue.. Y, N")
                if var.lower() == 'y':
                    self.__init__()
                else:
                    exit()

            guess = input("Guess a letter ->")

            if guess in the_word and guess not in letters_used:
                print("As it turns out, your guess was RIGHT!")
                letters_used += "," + guess
                print("Progress: " + self.progress_updater(guess, the_word, progress))
                print("Letter used: " + letters_used)
            elif guess not in the_word and guess not in letters_used:
                guesses += 1
                letters_used += "," + guess
                print("Progress: " + "".join(progress))
                print("Letter used: " + letters_used)
            else:
                print("That's the wrong letter, you wanna be out here all day?")
                print("Try again!")

                self.__init__()

    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
                i += 1
            else:
                i += 1

        return "".join(progress)

game = Hangman()