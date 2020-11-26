import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('NAVER', '2019-01-02')

# 20개 종가를 이용해서 평균을 구한다.
df['MA20'] = df['close'].rolling(window=20).mean()
# 20개 종가를 이용해서 표준편차를 구한 뒤 stdde 칼럼으로 df에 추가한다. 
df['stddev'] = df['close'].rolling(window=20).std()
# 중간 볼린저 밴드 + (2 x 표준편차)를 상단 볼린저 밴드로 계산한다. 
df['upper'] = df['MA20'] + (df['stddev'] * 2)
# 중간 볼린저 밴드 - (2 x 표준편차)를 하단 볼린저 밴드로 계산한다. 
df['lower'] = df['MA20'] - (df['stddev'] * 2)
# 위는 19번째 행까지 NaN 이므로 값이 있는 20번째 행부터 사용한다.
df = df[19:]

plt.figure(figsize=(9, 5))
# x좌표 df.index에 해당하는 종가를 y좌표로 설정해 파란색(#0000ff) 실선으로 표시한다.
plt.plot(df.index, df['close'], color='#0000ff', label='Close')
# x좌표 df.index에 해당하는 상단 볼린저 밴드값을 y좌표로 설정해 검은 실선(r--)으로 표시한다.
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
# 상단 볼린저 밴드와 하단 볼린저 밴드 사이를 회색으로 칠한다.
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
plt.legend(loc='best')
plt.title('NAVER Bollinger Band (20 day, 2 std)')
plt.show()