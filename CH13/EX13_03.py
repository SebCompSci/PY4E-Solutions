#13.03 Using Web Services
#Write a program that prompts for a location, contacts a web service, retrieves the JSON and retrieves the first 'place_id' from the JSON.
#A 'place_id' is a textual identifier that uniquely identifies a place as within Google maps.
#To complete this assignment you should use this API endpoint that has a static subset of the Google Data:
# 'http://py4e-data.dr-chuck.net/json?'
#This API uses the same parameter (address) as the Google API.
#This API has no rate limit so you can test as often as you like,
#If you visit the URL with no parameters you get 'No address...' response.
#To call the API, you need to include a 'key=' parameter and provide the address via the 'address=' parameter that is properly URL encoded using the 'urllib.parse.urlencode()' function.

import urllib.request, urllib.parse
import json

api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'
address = 'University of Ottawa'

parms = dict()
parms['address'] = address
parms['key'] = api_key

url = service_url + urllib.parse.urlencode(parms)
fhand = urllib.request.urlopen(url).read().decode()

js = json.loads(fhand)
place_id = js['results'][0]['place_id']
print(place_id)
