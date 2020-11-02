import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
df = mk.get_daily_price('005930', '2017-07-10', '2018-06-30')

plt.figure(figsize=(9,6))
plt.subplot(2, 1, 1)
plt.title('Samsung Electronics (Investar Data)')
plt.plot(df.index, df['Close'], 'c', label='Close')
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['Volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()