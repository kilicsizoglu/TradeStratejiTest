from ApiKeyClass import ApiKeyClass
from ApiKeyReader import readTAApiKey, writeTAApiKey, readBinanceApiKey, \
    writeBinanceApiKey


def ReadApiKey():
    taapikey = ''
    binanceapikey = ''
    binancesecret = ''
    binancepassphrase = ''
    binanceapidata = readBinanceApiKey()
    if binanceapidata is None:
        print('No Binance API key found. Please enter your API key, secret and passphrase.')
        binanceapikey = input('API key: ')
        binancesecret = input('Secret: ')
        writeBinanceApiKey(binanceapikey, binancesecret)
    else:
        print('Binance API key found. Using it.')
        binanceapikey = binanceapidata['apiKey']
        binancesecret = binanceapidata['secret']

    taapikeydata = readTAApiKey()
    if taapikeydata is None:
        print('No TAAPI API key found. Please enter your API key.')
        taapikey = input('API key: ')
        writeTAApiKey(taapikey)
    else:
        print('TAAPI API key found. Using it.')
        taapikey = taapikeydata['apikey']
    apikey = ApiKeyClass()
    apikey.binance_api_key = binanceapikey
    apikey.binance_api_secret = binancesecret
    apikey.ta_api_api_key = taapikey
    return apikey
