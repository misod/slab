import requests, flask, psutil, time, re

from random import randint
UUID = randint(0, 100000)
patToFile = "file_ip.txt"
fileStream = open(patToFile, 'r')
UUID_str = str(UUID)
ip_to_master = ''

try:
    with fileStream as openFile:
        for line in openFile:
            if line != '\n':
                ip_to_master = re.sub('[^0-9.]+', '', line)
                print ip_to_master
except Exception as e:
    print "nu blev det GALET"
    print e
finally:
    fileStream.close()

url = 'http://'+ip_to_master+':5000/slave/'+UUID_str+'/'
print url
for i in range(100):
    cpu = psutil.cpu_percent(interval=1, percpu=False)
    cpu_in_string = str(cpu)
    r = requests.get(url+cpu_in_string)
    response_json = r.json()
    print response_json
    time.sleep(2)
