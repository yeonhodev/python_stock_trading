# 앞에서 셋이 다른 반복자료형 보다 검색 시간이 훨씬 빠르다고 했는데, 이 말이 사실인지 실제로 확인해 보자. 일반적으로 파이썬 프로그램 성능 측정에 표준 라이브러리 timeit을 사용한다. 
#timeit(테스트 구분, setup=테스트 준비 구문, number=테스트 반복 횟수)

# 순회 속도 비교하기
# setup 구문에서 0부터 9999까지 정수 1만개를 원소로 갖는 리스트, 튜플, 셋을 생성한 후, 각 반복 자료형 별로 모든 원소를 처음부터 끝까지 순회(for ~ in ~)하는 동작을 1000번 반복하는 데 걸릴 총 시간을 비교 해 보자. 
import timeit

iteration_test = """
for i in itr :
  pass
"""
print(timeit.timeit(iteration_test, setup='itr = list(range(10000))', number=10000))

print(timeit.timeit(iteration_test, setup='itr = tuple(range(10000))', number=10000))

print(timeit.timeit(iteration_test, setup='itr = set(range(10000))', number=10000))