file = open("fun.txt","r")
mylist = []
for line in file:
    words = line.split()
    for word in words:
        if word.isalnum():
            mylist.append(word)

#print(mylist)
my_dict = {}

for str1 in mylist:
    if my_dict.__contains__(str1):
        count = my_dict.get(str1)
        count = count+1
        my_dict.update({str1:count})
    else:
        my_dict.update({str1: 1})


#dict2 = sorted(my_dict.items())
#print(my_dict)
file = open("fun2.txt","w")
for key, value in my_dict.items():
    sdf = str(value)
    text = "word "+key+"count "+ sdf +"\n"
    #print(text)
    file.write(text)




