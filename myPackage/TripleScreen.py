import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('엔씨소프트', '2017-01-01')

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

# 14일 동안의 최댓값을 구한다. min_periods=1을 지정할 경우, 14일 기간에 해당하는 데이터가 모두 누적되지 않았더라도 최소 기간인 1일 이상의 데이터만 존재하면 최댓값을 구하라는 의미다. 
ndays_high = df.high.rolling(window=14, min_periods=1).max()
# 14일 동안의 최솟값을 구한다. min_periods=1로 지정하면, 14일 치 데이터 모두 누적되지 않았더라도 최소 기간인 1일 이상의 데이터만 존재하면 최솟값을 구하라는 의미다. 
ndays_low = df.low.rolling(window=14, min_periods=1).min()

# 빠른 선 %K를 구한다. 
fast_k = (df.close - ndays_low) / (ndays_high - ndays_low) * 100
# 3일 동안 %K의 평균을 구해서 느린 선 %D에 저장한다. 
slow_d = fast_k.rolling(window=3).mean()
# %K와 %D로 데이터프레임을 생성한 뒤 결측치는 제거한다. 
df = df.assign(fast_k=fast_k, slow_d=slow_d).dropna()

plt.figure(figsize=(9, 9))
p1 = plt.subplot(3, 1, 1)
plt.title('Triple Screen Trading (NCSOFT)')
plt.grid(True)
# ohlc의 숫자형 일자, 시가, 고가, 저가, 종가 값을 이용해서 캔들 차트를 그린다. 
candlestick_ohlc(p1, ohlc.values, width=6, colorup='red', colordown='blue')
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['ema130'], color='c', label='EMA130')
for i in range(1, len(df.close)):
    # 130일 이동 지수평균이 상승하고 %D가 20 아래로 떨어지면 
    if df.ema130.values[i-1] < df.ema130.values[i] and df.slow_d.values[i-1] >= 20 and df.slow_d.values[i] < 20:
        # 빨간색 삼각형으로 매수 신호를 표시한다. 
        plt.plot(df.number.values[i], 250000, 'r^')
    # 130일 이동 지수평균이 하락하고 %D가 80 위로 상승하면
    elif df.ema130.values[i-1] > df.ema130.values[i] and df.slow_d.values[i-1] <= 80 and df.slow_d.values[i] > 80:
        # 파란색 삼각형으로 매수 신호를 표시한다. 
        plt.plot(df.number.values[i], 250000, 'bv')
plt.legend(loc='best')

p2 = plt.subplot(3, 1, 2)
plt.grid(True)
p2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.bar(df.number, df['macdhist'], color='m', label='MACD-Hist')
plt.plot(df.number, df['macd'], color='b', label='MACD')
plt.plot(df.number, df['signal'], 'g--', label='MACD-Signal')
plt.legend(loc='best')

p3 = plt.subplot(3, 1, 3)
plt.grid(True)
p1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot(df.number, df['fast_k'], color='c', label='%K')
plt.plot(df.number, df['slow_d'], color='k', label='%D')
# Y축 눈금을 0, 20, 80, 100으로 설정하여 스토캐스틱의 기준선을 나타낸다.
plt.yticks([0, 20, 80, 100])
plt.legend(loc='best')
plt.show()