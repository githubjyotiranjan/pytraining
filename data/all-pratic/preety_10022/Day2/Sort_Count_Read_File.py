from collections import Counter
import operator
import re
file=open("Sort_Count_Read.txt","r")
outputfile_refresh=open("Sort_Count_OutputFile.txt","w")
outputfile_refresh.write("{:15}{:3}\n".format("word","Count"))
outputfile_refresh.close()
outputfile=open("Sort_Count_OutputFile.txt","a+")
rx = "[.,;:\!)(]+"
D1={}
wordcount = Counter(file.read().split())
for k,v in wordcount.items():
 k = re.sub(rx, "", k.strip())
 D1[k] = v
print(D1)
print("*"*18)
print("*"*18)
print("{:15}{:3}".format("word","Count"))
outputfile.write("*"*18)
outputfile.write("\n")
print("*"*18)
for w in sorted(D1, key=D1.get, reverse=False):
 outputfile.write("{:15}{:3}\n".format(w,D1[w]))
 print("{:15}{:3}".format(w,D1[w]))
outputfile.close()











