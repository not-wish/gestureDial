import asyncio
import requests
from bleak import BleakClient

ADDRESS = "D5:4D:D9:7B:CA:75"
CHAR_UUID = "2A56"


def getWeather():
    respone = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=16.514&longitude=80.516&current=weather_code&timezone=auto&forecast_days=1"
    )
    data = respone.json()
    return data


def combo_handler(combo: int):
    if combo == 121:
        print("Temperature of Amaravati: ", getWeather(), "Celcius")


def notification_handler(sender, data):
    combo = int.from_bytes(data, "little")
    print("Gesture combo: ", combo)
    combo_handler(combo)


async def main():
    print("Started Monitoring!")
    async with BleakClient(ADDRESS) as client:
        await client.start_notify(CHAR_UUID, notification_handler)

        while True:
            await asyncio.sleep(1)


asyncio.run(main())
