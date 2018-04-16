# A python code without pprint
import requests
 
def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    resp = requests.get(url, params = {'address': address})
    return resp.json()
 
# calling geocode function
data = geocode('India gate')
 
# printing json response
print(data)