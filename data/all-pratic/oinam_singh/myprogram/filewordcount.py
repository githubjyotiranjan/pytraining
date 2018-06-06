file=open("tmpread.txt","r")

#for line in file:
 #   print(line)

file.close()
lines = {}
list1=list();
with open('tmpread.txt') as file:
   # lines = file.read().splitlines()
    #words = lines.split(" ")
    #print(words)
    for line in file:
        line = line.strip()
        #words = line.split(" ")
        words = line.split()
        #print(words)
        for word in words:
            list1.append(word)
           #print( word , end =' ')

#lines.append(line)
list1.sort();
var='';
listCnt=[]
cnt=1;
dict1 = {}
for l in list1:
    dict1[l]=[]
    if var==l:
        cnt = cnt + 1
        dict1[l].append(cnt)
    else:
        cnt=1
        var=l
        dict1[l].append(cnt)
   # print(l)
print(dict1)
