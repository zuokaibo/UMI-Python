import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http: //map.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address':address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure')
        print(data)
        continue

    print(json.dumps(js, indent = 4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location=js['results'][0]['formatted_address']
    print(location)


# above code is fine, nothing wrong with the code, but we need to key
# to authenticate the api,
# You need an API key. Otherwise it won't work.
#
# To get an API Key you have to go to this webpage
# https://cloud.google.com/maps-platform/#get-started
# and pick the products you need. Also select or create a
# project and finally you have to set up a billing account.
# Unfortunately it isn't for free as far as I know.
