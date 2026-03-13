import asyncio
import requests
from bleak import BleakClient
import json
import subprocess
import pyperclip
import webbrowser
import os

ADDRESS = "D5:4D:D9:7B:CA:75"
CHAR_UUID = "2A56"


def getDataMap():
    with open("dataMap.json", "r") as f:
        dataMap = json.loads(f.read())

    return dataMap


def data_handler(combo: int):
    global dataMap
    if str(combo) in dataMap:
        print(f"combo : {dataMap[str(combo)]}")
        # func = getattr(ActionLibrary, dataMap[str(combo)])
        # func()
        script_path = f"./actions/{dataMap[str(combo)]}.py"
        if os.path.exists(script_path):
            subprocess.Popen(["python3", script_path])
        else:
            print("Script doesn't exist or wrong name!")
    else:
        print("Gesture is not mapped to anything yet.")


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
            dataMap = getDataMap()
            await asyncio.sleep(1)


asyncio.run(main())
