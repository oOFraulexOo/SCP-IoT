import requests # http://docs.python-requests.org/en/master/
import psutil   # https://pypi.python.org/pypi/psutil
import time 
import json

deviceAlternateId = '?'               # the device Alternate ID
sensorAlternateId = '?'               # the sensor Alternate ID
capabilityAlternateId = '?'       # the capability Alternate ID
tenant = 'd389b179-421b-45a1-8eae-4efa74113a58.eu10.cp.iot.sap' # the IoT Service Host Name

start = 'https://'
main = '/iot/gateway/rest/measures/'
postAddress = (start + tenant + main + deviceAlternateId)

print ('Posting to:', postAddress)

def readsensors():
    global d_pctCPU
    d_pctCPU = psutil.cpu_percent(percpu=False, interval = 1)

    return

def postiotcf ():
    global d_pctCPU

    s_pctCPU = str(d_pctCPU)
    d_tstamp = time.asctime()

    print("\nValues to post: ", d_pctCPU, d_tstamp)

    bodyJson =      {
                "capabilityAlternateId":capabilityAlternateId,
                "sensorAlternateId":sensorAlternateId,
                "measures":[s_pctCPU]
                    }

    data = json.dumps(bodyJson)
    #uncomment the line below to see the JSON being sent
    print (str(bodyJson))

    headers = {'content-type': 'application/json'}
    # uncomment below 3 lines to send to SCP
    r = requests.post(postAddress,data=data, headers = headers,cert=('certificate.pem', 'certificate.key'), timeout=5)
    responseCode = r.status_code
    print ("==> HTTP Response: %d" %responseCode)

try:
	while(True):
		readsensors()
		postiotcf()
		time.sleep(2)
except KeyboardInterrupt:
	print("Stopped by the user!")