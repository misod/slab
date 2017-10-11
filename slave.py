import requests, flask
import psutil


url = 'http://130.239.81.63:5000/slave/34/'
cpu = psutil.cpu_percent(interval=1, percpu=True)
r = requests.get(url+cpu[0])
response_json = r.json()

print response_json
