import requests

url = "https://vellamo.tampere.fi/api/v1/area/hakametsa.geojson"
response = requests.get(url, verify = False)
print (response.text)
