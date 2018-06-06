file = open("E:\Jennifer\silly.txt","r")
words = file.read()
splitLines = words.split(" ")
len(splitLines)


wordsDict = {'mydict': 0}
for i in range(0, len(splitLines)):
    key = splitLines[i].lower()
    key = key.replace(".", "").replace(",", "")
    if wordsDict.get(key) == None:
        count = 0;
    else:
        count = wordsDict.get(key)
    wordsDict.update({key: count+1})

wordsDict.pop('mydict')
sorted(wordsDict.items())

file = open("E:\Jennifer\dict.txt","w")
dictToString = "%s"%sorted(wordsDict.items())
print(dictToString)
file.write(dictToString)

