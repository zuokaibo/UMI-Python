import urllib.parse
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import ssl

# #ctx code means ignore all errors or irregular experission
# # must put context = ctx in line 14
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))