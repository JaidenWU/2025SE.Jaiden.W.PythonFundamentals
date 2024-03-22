#Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
#  Queries the API for the CoinDesk Bitcoin Price Index, which returns a JSON object, 
#  among whose nested keys is the current price of Bitcoin as a float
#Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a thousands separator.


import requests
import sys 
import json

try:
    rbitcoin = sys.argv[1]
    rbitcoin = float(rbitcoin)
except (ValueError, IndexError):
    print("Invalid Input")
    sys.exit()

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    o = r.json()       
    bitcoinRate = o["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit()

bitcoinPrice = rbitcoin * bitcoinRate
print(f"${bitcoinPrice:,.4f}")