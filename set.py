# set은 중복이 없는 원소 집합을 나타낸다. 
s = {'A', 'P', 'P', 'L', 'E'}
print(s) # {'A', 'P', 'E', 'L'}

# 한 가지 기억할 점은 반드시 우리가 생성한 순서대로 원소가 저장되지는 않는다는 점이다. 
mySet = {'B', 6, 1, 2}
print(mySet)

# Set 내부에 특정 원소가 존재하는지 검사하려면 다음과 같이 if ~ in ~ 비교 구문으로 확인하면 된다. Set은 다른 반복 자료형 보다 훨씬 빨리 원소의 존재 여부를 검사 할 수 있다. 
if 'B' in mySet:
  print("'B' exists in", mySet)

# Set의 원소들은 인덱싱이 불가능한 대신, 원소들의 교집합, 합집합, 차집합을 구할 수 있다. 
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

print(setA & setB) # setA.intersection(setB)
print(setA | setB) # setA.union(setB)
print(setA - setB) # setA.difference(setB)
print(setB - setA) # setB.difference(setA)

# 아쉽게도 셋은 반복 자료형처럼 리터럴로 원소가 없는 생태에서 생성할 수 없다. s = {}으로 생성하면 실제로는 딕셔너리가 생성되니 주의하자. 빈 셋은 s = set()으로 생성해야 한다. 
ls2 = [] # ls = list()와 같은 결과
d = {} # d = dict()와 같은 결과
t = () # t = tuple()과 같은 결과

# 중복 없는 셋의 특징을 이용하면 다음처럼 리스트에서 중복 원소를 간단히 제거할 수 있다. 
ls2 = [1, 3, 5, 2, 2, 3, 4, 2, 1, 1, 1, 1, 5]
print(list(set(ls2)))