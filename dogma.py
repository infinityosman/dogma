import requests
import time
from datetime import datetime

import config



countlimit=23
count=datetime.now().hour
while True:
    try:
        dogmaapi = requests.get('https://api.wemixplay.com/info/v1/coin-detail?symbol=DOGMA', json={"key": "value"})
        DOGMA = dogmaapi.json()['data']['priceData']['price']
        dogmabozuk = round(DOGMA,4)
        print(dogmabozuk)

        droneapi = requests.get('https://api.wemixplay.com/info/v1/coin-detail?symbol=DRONE', json={"key": "value"})
        drone = droneapi.json()['data']['priceData']['price']
        dronebozuk = round(drone,4)
        print(dronebozuk)

        dt = datetime.now()
        if(count==countlimit):
                count=8
        if(dt.hour==count):
            payload = {
            "app_key": config.app_key, 
            "app_secret": config.api_key,
            "target_type": "app",
            "content": "Dogma = {0} Drone = {1}".format(dogmabozuk,dronebozuk)
            }

            r = requests.post("https://api.pushed.co/1/push", data=payload)
            count+=1

            

        if(dogmabozuk >= 0.90):
            payload = {
            "app_key": config.app_key,
            "app_secret": config.api_key,
            "target_type": "app",
            "content": "Dogma 90 sentin üzerinde !\0 Dogma = {0} Drone = {1}".format(dogmabozuk,dronebozuk)
            }

            r = requests.post("https://api.pushed.co/1/push", data=payload)

        time.sleep(60)
    except:
        print("Bir hata oluştu!")

    