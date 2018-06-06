file=open("content.txt","r")
wordcount={}
for w in file.read().split():
    if w not in wordcount:
        wordcount[w] = 1
    else:
        wordcount[w] =wordcount[w]+1
print (w,wordcount)

for item in wordcount.items():
    print("{}\t{}".format(*item))

file.close();