# 최대 손실 낙폭 - MDD(Maximum Drawdown)은 특정 기간에 발생한 최고점에서 최저점까지 가장 큰 손실을 의미한다. 퀀트 투자에서는 수익률을 높이는 것 보다 MDD를 낮추는 것이 더 낫다고 할 만큼 중요한 지표로서, 특정기간 동안 최대한 얼마늬 손실이 날 수 있는지를 나타낸다. 
# MDD = (최저점 - 최고점) / 최저점

# KOSPI(Korea Composite Stock Price Index, 한국종합주가지수)는 1983년 부터 발표되었으며, 1980년 1월 4일에 상장된 모든 종목의 시가 총액을 기준 지수 100포인트로 집계한다. 따라서 KOSPI 지수 2500은 한국 증시가 1980년 당시보다 25배 올랐음을 나타낸다. 
# KOSPI는 1994년 1145.66 포인트에서 1998년 277.37 포인트까지 4년동안 무려 75.8%가 하락했는데, 이 기간 MDD는 -75.8%이다. 전체 주식 시장이 1/4 토막 난 것이 KOSPI 역사상 최대 손실 낙폭이라고 할 수 있다. 

# 서브프라임 당시의 MDD - 야후 파이넨스로부터 2004년부터 현재까지의 KOSPI 지수 데이터를 다운로드 받아서 KOSPI의 MDD를 구해보자. MDD를 구하려면 기본적으로 rolling() 함수에 대해 알아야 한다. 

# 시리즈.rolling(윈도우 크기 [, min_periods=1]) [.집계 함수()]
# rolling() 함수는 시리즈에서 윈도우 크기에 해당하는 개수만큼 데이터를 추출하여 집계 함수에 해당하는 연산을 실시한다. 집계 함수로는 최댓값 max(), 평균값 mean(), 최솟값 min()을 사용할 수 있다. min_periods를 지정하면 데이터 개수가 윈도우 크기에 못미치더라도 min_periods로 지정한 개수만 만족하면 연산을 수행한다. 

# 다음은 야후 파이넨스에서 KOSPI 지수 데이터를 다운로드 한 뒤 rolling() 함수를 이용하여 1년 동안 최댓값과 최소값을 구하여 MDD를 계산하는 예이다. 

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import matplotlib.pyplot as plt

kospi = pdr.get_data_yahoo('^ks11', '2004-01-04') # KOSPI 지수 데이터를 다운로드 한다. KOSPI 지수의 심볼은 ^KS11이다. 

window = 252 # 산정 기간에 해당하는 window 값은 1년 동안 개장일을 252일로 어림잡아 설정했다. 
peak = kospi['Adj Close'].rolling(window, min_periods=1).max() # KOSPI 종가 갈럼에서 1년(거래일 기준) 기간 단위로 최고치 peak를 구한다. 
drawdown = kospi['Adj Close']/peak - 1.0 # drawdown은 최고치(peak) 대비 현재 KOSPI 종가가 얼마나 하락했는지를 구한다. 
max_dd = drawdown.rolling(window, min_periods=1).min() # drawdown에서 1년 기간 단위로 최저치 max__dd를 구한다. 마이너스값이기 때문에 최저치가 바로 최대 손실 낙폭이 된다. 

plt.figure(figsize=(9, 7))
plt.subplot(211) # 2행 1열 중 1행에 그린다. 
kospi['Close'].plot(label='KOSPI', title='KOSPI MDD', grid=True, legend=True)
plt.subplot(212) # 2행 1열 중 2행에 그린다. 
drawdown.plot(c='blue', label='KOSPI DD', grid=True, legend=True)
max_dd.plot(c='red', label='KOSPI MDD', grid=True, legend=True)
plt.show()

# 정확한 MDD는 min()함수로 구한다. 
print(max_dd.min())

# MDD를 기록한 기간을 구하려면 다음과 같이 인덱싱 조건을 적용하면 된다. 
print(max_dd[max_dd==-0.5453665130144085])