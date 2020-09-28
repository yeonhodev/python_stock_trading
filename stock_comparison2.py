# 그래프 출력
# plot(x, y, 마커 형태 [, label='Label'])
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

import matplotlib.pyplot as plt

plt.plot(sec.index, sec.Close, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft.Close, 'r--', label="Microsoft")
plt.legend(loc='best') # 범례를 best로 지정하면, 그래프가 표시되지 않는 부분을 찾아서 적절한 위치에 범례를 표시해준다.
plt.show()

# 일간 변동률(daily percent change)로 주가 비교하기
# R(오늘 변동률) = ((R(오늘 종가) - R(어제 종가) / R(어제 종가)) * 100
# 위의 수학식을 파이썬 코드로 옮기는 데 시리즈 모듈에서 제공하는 shift() 함수를 사용한다. 
print(type(sec['Close']))

# 삼성전자 종가 칼럼의 데이터 확인
print(sec['Close'])

# shift() 함수는 데이터를 이동시킬 때 사용하는 함수로, 인수로 n을 줄 경우 전체 데이터가 n행씩 뒤로 이동한다. 
print(sec['Close'].shift(1))

# 위의 수학식을 파이썬 코드로 표현
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
print(sec_dpc.head())

# 첫 번 째 일간 변동률의 값이 NaN인데, 향후 계산을 위해 NaN을 0으로 변경할 필요가 있다. 
sec_dpc.iloc[0] = 0 # 인티저 로케이션 인덱서를 사용해서 시리즈의 첫 번째 데이터를 0으로 변경한다. 
print(sec_dpc.head())

# 마이크로 소프트 데이터 프레임도 동일하게 처리해준다. 
msft_dpc = (msft['Close'] / msft['Close'].shift(1) - 1) * 100
msft_dpc.iloc[0] = 0
print(msft_dpc.head())

# Histogram은 frequency distribution을 나타내는 그래프로서, 데이터 값 들에 대한 구간별 빈도수를 막대 형태로 나타낸다. 이 때 구간 수를 bins라고 하는데 hist() 함수에서 사용되는 bins의 기본값은 10이다. 빈스에 따라 그래프 모양이 달라지므로 관측한 데이터 특성을 잘 보여주도록 빈스값을 정해야 한다. 삼성전자 주식 종가의 일간 변동률을 히스토그램으로 출력해보자. 맷플롯립에서 히스토그램은 hist() 함수를 사용한다. 삼성전자의 일간 변동률을 18개 구간으로 나누어 빈도수를 표시한다. 

import matplotlib.pyplot as plt
sec_dpc = (sec['Close'] / sec['Close'].shift(1) - 1) * 100
sec_dpc.iloc[0] = 0
plt.hist(sec_dpc, bins=18)
plt.grid(True)
plt.show()
# 출력된 결과를 보면 삼성전자 일간 변동률 분포가 0 bin을 기준으로 좌우 대칭적이다. 정규분포 형태와 비슷하다. 엄밀히 얘기하자면, 주가 수익률은 정규분포보다 중앙 부분이 더 뾰족하고, 양쪽 꼬리는 더 두터운 것으로 알려져 있다. 이를 각각 급첨분포(leptokurtic distribution)와 팻 테일(fat tail)이라 부른다. 

# 주가 수익률이 급첨분포를 나타낸다는 것은 정규분포와 비교했을 때 주가의 움직임이 대부분 매우 작은 범위 안에서 발생한다는 것을 의미한다. 그리고 두꺼운 꼬리를 가리키는 팻 테일은 그래프가 좌우 극단 부분에 해당하는 아주 큰 가격 변동이 정규분포보다 더 많이 발생한다는 의미다. 시리즈의 describe() 매서드를 이용하면 평균과 표준편차를 확인할 수 있다. 
print(sec_dpc.describe())

# 일간 변동률 누적합 구하기
# sec_dpc는 일간 변동률이기 때문에 종목별로 전체적인 변동률을 비교해보려면, 일간 변동률 누적합(Cumulative Sum)을 계산해야 한다. 누적합은 시리즈에서 제공하는 cumsum() 함수를 이용하여 구할 수 있다. 
sec_dpc_cs = sec_dpc.cumsum() # 일간 변동률의 누적합을 구한다. 
print(sec_dpc_cs)

