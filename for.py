for i in [1, 2, 3]:
  print(i)

# range(시작값, 멈춤값, 증가값) : 멈춤값으로 주어진 수는 반복할 범위에 포함되지 않는다.
for i in range(1, 7, 2):
  print(i)

# enumerate([반복자료형], 인덱스의_시작값) : 각각의 반복과정에서 아이템 인덱스를 구할수 있어서 편리하다. 시작값을 생략하면 첫번째 인덱스는 0부터 시작한다.
FAANG = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']
for idx, symbol in enumerate(FAANG, 1):
  print(idx, symbol)