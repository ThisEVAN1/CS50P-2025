import requests
import sys

try:
    amount = float(sys.argv[1])
    api = requests.get(
        # Remember to change 'YOUR_API_KEY' to your API key!
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOUR_API_KEY"
    )
    api = api.json()
    price = amount * float(api["data"]["priceUsd"])
    print(f"${price:,.4f}")
except requests.RequestException:
    sys.exit("RequestException")
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")
