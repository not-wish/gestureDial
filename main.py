import asyncio
import requests
from bleak import BleakClient
import json
import subprocess
import pyperclip
import webbrowser

ADDRESS = "D5:4D:D9:7B:CA:75"
CHAR_UUID = "2A56"


class ActionLibrary:
    @staticmethod
    def temperatureInfo():
        respone = requests.get(
            "https://api.open-meteo.com/v1/forecast?latitude=16.514&longitude=80.516&current=temperature_2m&timezone=auto&forecast_days=1"
        )
        data = respone.json()["current"]["temperature_2m"]
        print(f"Amaravati's temprature: {data} degree Celcius")

    def open_firefox():
        subprocess.run(["firefox", "&"], shell=True)

    def github_search(url="https://duckduckgo.com/?t=ffab&q="):
        query = (
            "https://duckduckgo.com/?t=ffab&q="
            + "site:github.com"
            + "+"
            + pyperclip.paste()
        )
        webbrowser.open_new_tab(query)


def getDataMap():
    with open("dataMap.json", "r") as f:
        dataMap = json.loads(f.read())

    return dataMap


def data_handler(combo: int):
    global dataMap
    if str(combo) in dataMap:
        print(f"combo : {dataMap[str(combo)]}")
        func = getattr(ActionLibrary, dataMap[str(combo)])
        func()


def notification_handler(sender, data):
    combo = int.from_bytes(data, "little")
    print("Gesture combo: ", combo)
    data_handler(combo)


dataMap = dict()


async def main():
    global dataMap
    dataMap = getDataMap()
    if dataMap is None:
        print("Error getting data map!")
        return
    print(dataMap)
    print("Successfully loaded data map!")
    print("--===Started Monitoring===--")
    async with BleakClient(ADDRESS) as client:
        await client.start_notify(CHAR_UUID, notification_handler)

        while True:
            await asyncio.sleep(1)


asyncio.run(main())
