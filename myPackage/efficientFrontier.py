import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2016-01-04', '2018-04-27')['close']

# 시총 상위 4 종목의 수익률을 비교하려면 종가 대신 일간 변동률로 비교를 해야 하기 때문에 데이터프레임에서 제공하는 pct_change() 함수를 사용해 4 종목의 일간 변동률을 구한다. 
daily_ret = df.pct_change()

# 일간 변동률의 평균값에 252를 곱해서 연간 수익률을 구한다. 252는 미국의 1년 평균 개장일로, 우리나라 실정에 맞게 다른 숫자로 바꾸어도 무방하다. 
annual_ret = daily_ret.mean() * 252

# 일간 리스크는 cov() 함수를 사용해 일간 변동률의 공분산으로 구한다.
daily_cov = daily_ret.cov()

# 연간 공분산은 일간 공분산에 252를 곱해 계산한다. 
annual_cov = daily_cov * 252

port_ret = []
# 시총 상위 4종목 비중을 다르게 해 포트폴리오 20,000개를 생성한다. 포트폴리오 수익률, 리스크, 종목 비중을 저장할 각 리스트를 생성한다. 
port_risk = []
port_weights = []

# Display results
print(daily_ret)
print(annual_ret)
print(daily_cov)
print(annual_cov)