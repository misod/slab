import requests, flask, psutil, time, re, signal, sys

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
except Exception as e:
    print "nu blev det GALET"
    print e
finally:
    fileStream.close()

def signal_handler(signal, frame):
        print('quitting')
        time.sleep(0.5)
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


url = 'http://'+ip_to_master+':5000/slave/'+UUID_str+'/'
print url
for i in range(5):
    cpu = psutil.cpu_percent(interval=5, percpu=False)
    cpu_in_string = str(cpu)
    r = requests.get(url+cpu_in_string)
    response_json = r.json()
    print response_json
    time.sleep(1)
