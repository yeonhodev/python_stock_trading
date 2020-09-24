# source: github.com/ranaroussi/yfinance
# get_data_yahoo(조회할 주식 종목 [, start=조회 기간의 시작일] [, end=조회 기간의 종료일])

# 삼성전자(005930.KS)와 마이크로소프트(MSFT)의 일별 주가 데이터를 다운받아 어떤 종복의 수익률이 더 좋았는지 확인한다
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override() # pdr_override() 함수와 pandas_datareader.data.get_data_yahoo() 함수를 사용하여 빠르게 데이터를 다운로드 할 수 있다.

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04') 
msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')

print(sec.head(10))

# Volume 칼럼 제거
tmp_msft = msft.drop(columns='Volume')
print(tmp_msft.tail())

# 인덱스 확인
print(sec.index)

# 칼럼 확인
print(sec.columns)