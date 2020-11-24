import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
stocks = ['삼성전자', 'SK하이닉스', '현대자동차', 'NAVER']
df = pd.DataFrame()
for s in stocks:
    df[s] = mk.get_daily_price(s, '2016-01-04', '2018-04-27')['close']

daily_ret = df.pct_change()
annual_ret = daily_ret.mean() * 252
daily_cov = daily_ret.cov()
annual_cov = daily_cov * 252

port_ret = []
port_risk = []
port_weights = []
sharpe_ratio = []

for _ in range(20000):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)

    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    # 포트폴리오의 수익률을 리스크로 나눈 값을 샤프 지수 리스트에 추가한다.
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns': port_ret, 'Risk': port_risk, 'Sharpe':sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weights[i] for weight in port_weights]
df = pd.DataFrame(portfolio)
# 샤프 지수 칼럼을 데이터프레임에 추가한다. 생성된 데이터프레임은 다음과 같다. 
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]

# 샤프 지수 칼럼에서 샤프 지숫값이 제일 큰 행을 max_sharpe로 정한다. 
max_sharpe = df.loc[df['Sharpe'] == df['Sharpe'].max()]
# 리스크 칼럼에서 리스크 값이 제일 작은 행을 min_risk로 정한다.
min_risk = df.loc[df['Risk'] == df['Risk'].min()]

# Return result looks wrong. Will need to be fixed. 
print(max_sharpe)
print(min_risk)

# 포트폴리오의 샤프 지수에 따라 컬러맵을 'viridis'로 표시하고 테두리는 검정(k)으로 표시한다. 
df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis', edgecolors='k', figsize=(11, 7), grid=True)
# 샤프 지수가 가장 큰 포트폴리오를 300 크기의 붉은 별표(*)로 표시한다.
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
# 리스크가 제일 작은 포트폴리오를 200 크기의 붉은 엑스표(x)로 표시한다. 
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.title('Portfolio Optimization')
plt.xlabel('Risk')
plt.ylabel('Expected Returns')
plt.show()

