dics = {}

with open('tmpread.txt') as file:

    for line in file:
        line = line.strip()

        #print(words)
        for word in line.split():
            if word not in dics:
                dics[word]=1;
            else:
                dics[word] += 1;


print(dics)
