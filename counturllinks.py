from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/known_by_Corbin.html"

#to repeat 7 times#
for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count + 1
        print(count)
        if count > 18:
            # print(tag.get('href', None))
            break
        url = tag.get('href', None)
print(url)