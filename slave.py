import requests


url = 'http://130.239.81.63:5000/slave/34/'

r = requests.get(url+'3')
response_json = r.json()

print response_json
