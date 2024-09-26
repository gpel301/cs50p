import requests
import sys
import json

try:
    n = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")



if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# elif not float(sys.argv[1]):
#     sys.exit("Command-line argument is not a number")

else:
    # response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(json.dumps(response.json(), indent = 2))
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        amount = o["bpi"]["USD"]
        result = (amount["rate_float"]) * n
        print(f"${result:,.4f}")

    except requests.RequestException:
        sys.exit("Something went wrong")

