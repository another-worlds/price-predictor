# Import modules
import backtrader as bt
import pandas as pd
from strategies import TestStrategy

# Init cerebro and set cash
cerebro = bt.Cerebro()
cerebro.broker.set_cash(1000000)

# Load data and pass to cerebro
data = pd.read_csv(filepath_or_buffer='../data/BITSTAMP_BTCUSD_DAY.csv', index_col='Date', parse_dates=True)
data.rename(columns={'Volume USD' : 'Volume'}, inplace=True) # Rename "Volume USD" column to "Volume" so backtrader recognizes it
data = data.reindex(index=data.index[::-1])
feed = bt.feeds.PandasData(dataname=data)

# load strategy
cerebro.addstrategy(TestStrategy)
cerebro.adddata(feed)

# run strategy
cerebro.run()
cerebro.plot()