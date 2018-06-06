import operator
from collections import OrderedDict
from collections import defaultdict
mydict = defaultdict(int)

with open('tmpread.txt') as file:
    for line in file:
        line = line.strip()
        for w in line.split():
            mydict[w] += 1
#sorted_x = sorted(dics.items(), key=operator.itemgetter(1))
print(mydict.items());
print(mydict.keys());
d_sorted_by_value = OrderedDict(sorted(mydict.items(), key=lambda x: x[1]))
print(d_sorted_by_value.items());
print(d_sorted_by_value.keys());

d_sorted_by_key = OrderedDict(sorted(mydict.items(), key=lambda x: x[0]))
print(d_sorted_by_key.items());
print(d_sorted_by_key.keys());
