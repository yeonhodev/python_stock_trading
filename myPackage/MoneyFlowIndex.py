# 고가, 저가, 종가의 합을 3으로 나눠서 중심 가격 TP(Typical Price)를 구한다.
df['TP'] = (df['high'] + df['low'] + df['close']) / 3
df['PMF'] = 0
df['NMF'] = 0
# range 함수는 마지막 값을 포함하지 않으므로 0부터 종가 개수 -2까지 반복한다. 
for i in range(len(df.close)-1):
    # i번째 중심 가격보다 i+1번째 중심 가격이 높으면
    # i+1번째 중심 가격과 i+1번째 거래량의 곱을 i+1번째 긍정적 현금 흐름 PMF(Positive Money Flow)에 저장한다.
    # i+1번째 부정적 현금 흐름 NMF(Negative Money Flow)값은 0으로 저장한다. 