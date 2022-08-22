import backtrader as bt

class TestStrategy(bt.Strategy):
    params = {
        'slow_ma' : 9,
        'fast_ma' : 13,
        'signal_ma' : 6
    }

    def __init__(self):
        self.macd = bt.ind.MACD(
            self.data.close,
            period_me1 = self.p.slow_ma,
            period_me2 = self.p.fast_ma,
            period_signal = self.p.signal_ma
        )

    def next(self):
        if self.position.size == 0:
            self.buy(size=self.broker.cash/self.data.close[0])