import sys
import requests
import json
import time
import math
import random

# replace these variables
deviceAlternateId = '?'               # the device Alternate ID
sensorAlternateId = '?'               # the sensor Alternate ID
capabilityAlternateId = '?'       # the capability Alternate ID
tenant = 'https://d389b179-421b-45a1-8eae-4efa74113a58.eu10.cp.iot.sap/iot/gateway/rest/measures/' # the IoT Service Host Name

postAddress = (tenant + deviceAlternateId)
print ('Posting to:', postAddress)

# Time intervall for polling the sensor data in seconds
timeIntervall = 5

# Number of iterations
iterations = 20

for x in range (0, iterations):

    try:
        print("")
        print("============================================")
        print("Reading sensor data ...")

        speed = random.randint(0,40)

        valueSpeed = round(speed,2)
        print("speed value = %f" %valueSpeed, "MpH")

        bodyJson =  {
                "capabilityAlternateId":capabilityAlternateId,
                "sensorAlternateId":sensorAlternateId,
                "measures":[valueSpeed]
                }

        data = json.dumps(bodyJson)
        headers = {'content-type': 'application/json'}
        r = requests.post(postAddress,data=data, headers = headers,cert=('certificate.pem', 'certificate.key'), timeout=5)
        responseCode = r.status_code
        print (str(bodyJson))
        print ("==> HTTP Response: %d" %responseCode)

        # wait timeIntervall [s] before reading the sensor values again
        time.sleep(timeIntervall)

    except IOError:
        print ("Error")