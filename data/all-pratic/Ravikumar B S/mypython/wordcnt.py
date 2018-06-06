from collections import OrderedDict
#from sortedcontainers import SortedDict
file=open("fun.txt","r")
wordcount={}

#line=file.read()
#print (line)
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
    #line = file.read()
print(wordcount.keys())
print(wordcount.values())
wordcount=OrderedDict(sorted(wordcount.items(),  key=lambda t:t[0]))
#wordcount=SortedDict(wordcount)
print(wordcount.keys())
for k, v in wordcount.items():
    print(k,v)