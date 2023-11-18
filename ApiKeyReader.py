import json
import os.path


def readBinanceApiKey():
    try:
        with open('binance-api-key.txt', 'r') as f:
            data = json.JSONDecoder().decode(f.read())
            if data['apiKey'] == '' or data['secret'] == '':
                return None
            else:
                return data
    except FileNotFoundError:
        return None


def writeBinanceApiKey(apiKey, secret):
    with open('binance-api-key.txt', 'w') as f:
        json.dump({'apiKey': apiKey, 'secret': secret}, f)


def writeTAApiKey(apikey):
    with open('ta-api-key.txt', 'w') as f:
        json.dump({'apikey': apikey}, f)


def readTAApiKey():
    try:
        with open('ta-api-key.txt', 'r') as f:
            data = json.JSONDecoder().decode(f.read())
            if data['apikey'] == '':
                return None
            else:
                return data
    except FileNotFoundError:
        return None
