from api_tool.crypto import get_crypto_price
from api_tool.quotes import get_quote
from api_tool.weather import get_weather


def main():
    print("Välj ett kommando: crypto | quote | weather | exit")

    while True:
        command = input("> ").strip().lower()

        if command in ("exit", "quit", "q"):
            print("Hejdå!")
            break

        if command == "crypto":
            get_crypto_price()

        elif command == "quote":
            get_quote()

        elif command == "weather":
            city = input("Ange en stad: ").strip()
            if not city:
                print("Du måste ange en stad.")
                continue
            get_weather(city)

        else:
            print("Okänt kommando. Välj: crypto | quote | weather | exit")


if __name__ == "__main__":
    main()
