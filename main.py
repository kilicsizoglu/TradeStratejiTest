from datetime import datetime

import pandas as pd
from binance import Client

import ApiKeyReadScript
import ApiKeyReader
import TradeStrateji.TradeStrateji_v1
import backtrader as bt


def main():

    key = ApiKeyReadScript.ReadApiKey()

    # Binance API ayarları
    api_key = key.binance_api_key
    api_secret = key.binance_api_secret

    client = Client(api_key, api_secret)

    # Binance'dan REEFUSDT verisini çek
    bars = client.get_historical_klines("REEFUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "31 Dec, 2021")

    # Veriyi Pandas DataFrame'e dönüştür
    df = pd.DataFrame(bars,
                      columns=['datetime', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
                               'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume',
                               'ignore'])
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)

    # Sadece gerekli sütunları seç
    df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)

    # Backtrader için veri kaynağı oluştur
    class BinanceData(bt.feeds.PandasData):
        params = (
            ('datetime', None),
            ('open', -1),
            ('high', -1),
            ('low', -1),
            ('close', -1),
            ('volume', -1),
        )

    # Backtesting ortamını kur
    cerebro = bt.Cerebro()
    cerebro.adddata(BinanceData(dataname=df))

    # Stratejiyi cerebro'ya ekle
    cerebro.addstrategy(TradeStrateji.TradeStrateji_v1.ADXRSIMACDStrategy)

    # Başlangıç sermayesini ayarla
    cerebro.broker.setcash(10000.0)

    # Backtesting'i başlat
    cerebro.run()

    # Backtesting'i Başlat
    print('Başlangıç Portföy Değeri: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Son Portföy Değeri: %.2f' % cerebro.broker.getvalue())


if __name__ == '__main__':
    main()
