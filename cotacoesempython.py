import pandas
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()

df = pdr.get_data_yahoo("TSLA", start="2020-01-01", end="2021-01-01")
print(df)