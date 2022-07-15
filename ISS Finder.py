import urllib.request
import json
import time
api_url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(api_url)
obj = json.loads(response.read())
lat = obj['iss_position']['latitude']
long = obj['iss_position']['longitude']
url = "https://www.openstreetmap.org/?mlat=" + str(lat) + "&mlon=" + str(long) +  "#map=5/" + str(lat) + "/" + str(long)
import webbrowser
webbrowser.open_new(url)