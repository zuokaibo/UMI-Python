# here we extract some information from webpage by using url

import urllib.request, urllib.parse, urllib.error
urlfile = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in urlfile:
    # decode() is transfering bytes(computer language, 0 and 1) to UTF8 language (human language), encode()
    #  transfering human language into computer language (byte)
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

newlist = list()
newdict = dict()
for key, value in counts.items():
    newdict = (value, key)
    newlist.append(newdict)
newlist = sorted(newlist, reverse=True)
print(newlist)






