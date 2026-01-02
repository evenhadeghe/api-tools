import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.RequestException:
        print("Kunde inte hämta väderdata")
