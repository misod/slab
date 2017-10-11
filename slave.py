import requests, flask
import psutil, time


url = 'http://130.239.81.63:5000/slave/34/'
for i in rage(10):
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    cpu_in_string = str(cpu[0])
    r = requests.get(url+cpu_in_string)
    response_json = r.json()
    print response_json
    time.sleep(2)
