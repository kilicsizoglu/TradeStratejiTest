import backtrader as bt


# Strateji Tanımı
class ADXRSIMACDStrategy(bt.Strategy):
    params = (
        ("adx_period", 14),
        ("rsi_period", 14),
        ("macd_fast", 12),
        ("macd_slow", 26),
        ("macd_signal", 9),
        ("adx_threshold", 25),
        ("rsi_upper", 70),
        ("rsi_lower", 30)
    )

    def __init__(self):
        self.adx = bt.indicators.AverageDirectionalMovementIndex(self.data, period=self.params.adx_period)
        self.rsi = bt.indicators.RSI(self.data, period=self.params.rsi_period)
        self.macd = bt.indicators.MACD(self.data, period_me1=self.params.macd_fast, period_me2=self.params.macd_slow,
                                       period_signal=self.params.macd_signal)

    def next(self):
        if self.adx[0] > self.params.adx_threshold and self.rsi[0] < self.params.rsi_lower and self.macd.macd[0] > \
                self.macd.signal[0]:
            self.buy()
        elif self.adx[0] > self.params.adx_threshold and self.rsi[0] > self.params.rsi_upper and self.macd.macd[0] < \
                self.macd.signal[0]:
            self.sell()
