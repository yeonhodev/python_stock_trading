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