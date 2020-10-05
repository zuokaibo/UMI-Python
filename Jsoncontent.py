import json
import urllib.request


url = input('enter url: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_929232.json"
print("retrieving: ", url)

jurl = urllib.request.urlopen(url).read()

info = json.loads(jurl)

count = 0
for item in info["comments"]:
    number = int(item["count"])
    count = count + number

print("Count: ", count)


