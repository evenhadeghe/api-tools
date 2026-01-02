import requests  
def get_crypto_price():

    url = "https://data-api.coindesk.com/info/v1/openapi"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        price = data["bpi"]["USD"]["rate"]
        print(f"Bitcoin price (USD): {price}")

    except requests.exceptions.RequestException as error:
        print_error("Kunde inte hämta kryptopris")
        print(error)
