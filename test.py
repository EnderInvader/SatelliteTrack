DAYS = 1
MIN_ELEVATION = 10

# NOAA19 NOAA18
SAT = [33591,28654]
FREQ = [137.100,137.9125]


from dotenv import dotenv_values
import requests
import json
from datetime import datetime
import geocoder


def get_elevation(lat, long):
	query = ('https://api.open-elevation.com/api/v1/lookup'
			 f'?locations={lat},{long}')
	r = requests.get(query).json()
	elevation = r['results'][0]['elevation']
	return elevation

def unix2str(unix):
	return datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')


#latlng = geocoder.ip('me').latlng
#elv = get_elevation(latlng[0],latlng[1])
#print([latlng,elv])


j = requests.get(f'https://api.n2yo.com/rest/v1/satellite/radiopasses/{SAT[0]}/{OBSERVER_LAT}/{OBSERVER_LNG}/{OBSERVER_ALT}/{DAYS}/{MIN_ELEVATION}/&apiKey={API_KEY}').json()

passes = j['passes']


print(unix2str(passes[0]['startUTC']))
print(unix2str(passes[0]['maxUTC']))
print(unix2str(passes[0]['endUTC']))

print()