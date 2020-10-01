# 최대 손실 낙폭 - MDD(Maximum Drawdown)은 특정 기간에 발생한 최고점에서 최저점까지 가장 큰 손실을 의미한다. 퀀트 투자에서는 수익률을 높이는 것 보다 MDD를 낮추는 것이 더 낫다고 할 만큼 중요한 지표로서, 특정기간 동안 최대한 얼마늬 손실이 날 수 있는지를 나타낸다. 
# MDD = (최저점 - 최고점) / 최저점

# KOSPI(Korea Composite Stock Price Index, 한국종합주가지수)는 1983년 부터 발표되었으며, 1980년 1월 4일에 상장된 모든 종목의 시가 총액을 기준 지수 100포인트로 집계한다. 따라서 KOSPI 지수 2500은 한국 증시가 1980년 당시보다 25배 올랐음을 나타낸다. 
# KOSPI는 1994년 1145.66 포인트에서 1998년 277.37 포인트까지 4년동안 무려 75.8%가 하락했는데, 이 기간 MDD는 -75.8%이다. 전체 주식 시장이 1/4 토막 난 것이 KOSPI 역사상 최대 손실 낙폭이라고 할 수 있다. 

# 서브프라임 당시의 MDD - 야후 파이넨스로부터 2004년부터 현재까지의 KOSPI 지수 데이터를 다운로드 받아서 KOSPI의 MDD를 구해보자. MDD를 구하려면 기본적으로 rolling() 함수에 대해 알아야 한다. 