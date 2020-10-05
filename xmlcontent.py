import urllib.request
import xml.etree.ElementTree as ET
import ssl

url = input("Enter url:")
if len(url) < 1:
    url ="http://py4e-data.dr-chuck.net/comments_929231.xml "
print("retrieving", url)

xml = urllib.request.urlopen(url).read()
print("retrieving", str(len(xml)), "characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Counts: ", str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)


print("sum:", accumulator)


