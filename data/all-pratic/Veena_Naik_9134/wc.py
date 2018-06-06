FILE_NAME = 'example.txt'

outputfile=open("output.txt","w")

wordCounter = {}

with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1

outputfile.write('{:15}{:3}\n'.format('Word','Count'))
outputfile.write('-' * 18)
outputfile.write('\n')

# printing the words and its occurrence.
for  w  in sorted(wordCounter,key=wordCounter.get,reverse=False):

     outputfile.write('{:15}{:3}'.format(w,wordCounter[w]))
     outputfile.write('\n')