class LetsPlay:
    LifeLeft = 0
    wordlength = 0

    def __init__(self, word):
        self.word = word
        LetsPlay.LifeLeft = 10

    def getresult(self):
     num = 0
     wordlen = len(self.word)
     for i in range(0, wordlen):
        inputletter: str = input("enter letter: ")
        arr = list(self.word)
        for j in range(num, len(arr)):
                if inputletter == arr[j]:
                    num += 1
                    break
                else:
                    LetsPlay.LifeLeft = LetsPlay.LifeLeft-1
                    print("wrong number , try again life left {}", LetsPlay.LifeLeft)
                    break
        break
test = LetsPlay("deepak")
test.getresult()
