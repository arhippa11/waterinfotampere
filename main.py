import requests
import json
import time
import os
from dotenv import load_dotenv
load_dotenv()
area = os.getenv("AREA")
while True:
    url = "https://vellamo.tampere.fi/api/v1/area/"+area+".geojson"
    response = requests.get(url, verify = False)
    print (response.text)

    response_simple = json.loads(response.text)
    ph = response_simple['properties']["ph"]
    rounded_ph = round(ph, 1)

    temp_c = response_simple['properties']["t"]
    rounded_temp_c = round(temp_c, 1)
    message = "pH: " + str(rounded_ph) + " Lämpötila: " + str(rounded_temp_c) + "°C"
    def send_discord_message(message):
        url_discord = os.getenv("DISCORD_WEBHOOK_URL")

        #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
        data = {
            "content" : message,
            "username" : "WaterInfo"
        }

        result = requests.post(url_discord, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)

    send_discord_message(message)
    print(message)
    print("Message sent")
    print("Waiting 60 minutes")
    time.sleep(3600)