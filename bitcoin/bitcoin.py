import json
import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")


try:
    argt = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")

try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    print('An error occured while fetching JSON')

o = response.json()
rate = float(o["bpi"]['USD']['rate'].replace(',',''))

amount = argt * rate

print(f"${amount:,.4f}")

