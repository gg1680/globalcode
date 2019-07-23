import geocoder
from geopy.geocoders import Nominatim

## remember to install libraries first:
# pip install geocoder
# pip install geopy

# get current coordinates
g = geocoder.ip('me')
print(g.latlng)

# read latitude and longitude into a point
lat, lng = g.latlng
point = f"{lat}, {lng}"

# get a geolocator
geolocator = Nominatim(user_agent="gjeta-test")

# read location from coordinates and get address
loc = geolocator.reverse(point)
print(loc.address)