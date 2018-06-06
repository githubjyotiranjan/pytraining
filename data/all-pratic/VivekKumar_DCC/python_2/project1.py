file = open("project.txt", "w")
file.write("India, also called the Republic of India, is a country in South Asia.\n It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world.\n It is bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast.\n It shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the northeast; and Bangladesh and Myanmar to the east.\n In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives.\n India's Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia. ")
file = open("project.txt", "r")
bob=file.read()
dog=bob.replace(",","")
dog1=dog.replace(".","")
dog2=dog1.replace("'","")
dog3=dog2.replace(";","")
mylist=dog3.split()
my_dict={}
for n in mylist:
    if not n in my_dict:
        my_dict[n]=mylist.count(n)
        #print(my_dict[n])
        #print(my_dict.items())
a = sorted(my_dict.items())
for i in a:
   print("{0}-------> {1}".format(i[0],i[1]))

