import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2017-01-01', '2020-12-01')

# 종가의 12주 지수 이동평균에 해당하는 60일 지수 이동평균을 구한다. 
ema60 = df.close.ewm(span=60).mean()
# 종가의 26주 지수 이동평균에 해당하는 130일 지수 이동평균을 구한다. 
ema130 = df.close.ewm(span=130).mean()
# 12주(60일) 지수 이동평균에서 26주(130일) 지수 이동평균을 빼서 MACD(Moving Average Convergence Divergence)선을 구한다. 
macd = ema60 - ema130
# MACD의 9주(45일) 지수 이동평균을 구해서 신호선으로 저장한다. 
signal = macd.ewm(span=45).mean()
# MACD선에서 신호선을 빼서 MACD 히스토그램을 구한다. 
macdhist = macd - signal

df = df.assign(ema130=ema130, ema60=ema60, macd=macd, signal=signal, macdhist=macdhist).dropna()
# 캔들 차트에 사용할 수 있게 날짜(date)형 인덱스를 숫자형을 변환한다. 
df['number'] = df.index.map(mdates.date2num)
ohlc = df[['number', 'open', 'high', 'low', 'close']]

plt.figure(figsize=(9, 7))
p1 = plt.subplot(2, 1, 1)
plt.title('Triple Screen Trading - First Screen (NCSOFT)')
plt.grid(True)
# ohlc의 숫자형 일자, 시가, 고가, 저가, 종가 값을 이용해서 캔들 차트를 그린다. 
candlestick_ohlc(p1, ohlc.values, width=6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
plt.legend(loc='best')

p2 = plt.subplot(2, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Hist')
plt.plot(df.number, df['macd'], color='b', label='MACD')
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
plt.legend(loc='best')
plt.show()