# 앞에서 셋이 다른 반복자료형 보다 검색 시간이 훨씬 빠르다고 했는데, 이 말이 사실인지 실제로 확인해 보자. 일반적으로 파이썬 프로그램 성능 측정에 표준 라이브러리 timeit을 사용한다. 
#timeit(테스트 구분, setup=테스트 준비 구문, number=테스트 반복 횟수)

# 순회 속도 비교하기
# setup 구문에서 0부터 9999까지 정수 1만개를 원소로 갖는 리스트, 튜플, 셋을 생성한 후, 각 반복 자료형 별로 모든 원소를 처음부터 끝까지 순회(for ~ in ~)하는 동작을 1000번 반복하는 데 걸릴 총 시간을 비교 해 보자. 
import timeit

iteration_test = """
for i in itr :
  pass
"""
# list
print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=10000))
# tuple
print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=10000))
# set
print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=10000))

# 검색속도 비교하기
# 다음은 표준 라이브러리인 random 모듈의 randint() 함수를 이용하여 0 이상 9999 이하의 임의의 난수를 생성한 후, 0부터 9999까지 정수 1만 개로 구성된 반복 자료형에 존재하는지 검색(if ~ in ~)하는 코드다.

search_test = """
import random
x = random.randint(0, len(itr)-1)
if x in itr:
  pass
"""
#임의의 난수를 검색하는 작업을 1000 번씩 반복해서 수행한 결과, 셋의 검색 속도가 리스트나 튜플보다 월등히 빠른 것으로 나타났다.

# set
print(timeit.timeit(search_test, setup='itr = set(range(10000))', number=10000))
# list
print(timeit.timeit(search_test, setup='itr = list(range(10000))', number=10000))
#tuple
print(timeit.timeit(search_test, setup='itr = tuple(range(10000))', number=10000))