import sys


from api_tool.crypto import get_crypto_price
from api_tool.quotes import get_quote 
from api_tool.weather import get_weather 

def main():
    if len(sys.argv) < 2:
        print("Välj ett kommando: crypto | quote | weather")
        return
    
    command = sys.argv[1]

    if command == "crypto":
        get_crypto_price()

    elif command == "quote":
        get_quote()

    elif command == "weather":
        if len(sys.argv) < 3:
            print("Ange en stad")
        else:
            get_weather(sys.argv[2])

    else:
        print("Okänt kommando")


if __name__ == "__main__":
    main()