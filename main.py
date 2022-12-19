import requests
from time import sleep

binance = 'https://api.binance.com/api/v3/ticker/price'
b_crypto = 'BTCUSDT'

wazirx = 'https://api.wazirx.com/api/v2/tickers'
w_crypto = 'btcusdt'

coinbase = 'NA'
kraken = 'NA'

def binance_info():

    bin_data = requests.get(binance)
    bin_resp = bin_data.json()

    print(bin_data.json())
    a = bin_resp[0]
    x = 0

    for each in bin_resp:
        print(bin_resp[x])
    x = x+1

    #print(a)

def wazirx_info():

    waz_data = requests.get(wazirx)
    waz_resp = waz_data.json()
    print(waz_resp)


binance_info()
#wazirx_info()