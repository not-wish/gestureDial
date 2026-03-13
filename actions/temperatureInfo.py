import requests


def temperatureInfo():
    respone = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=16.514&longitude=80.516&current=temperature_2m&timezone=auto&forecast_days=1"
    )
    data = respone.json()["current"]["temperature_2m"]
    print(f"Amaravati's temprature: {data} degree Celcius")


if __name__ == "__main__":
    temperatureInfo()
