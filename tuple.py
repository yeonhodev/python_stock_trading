# 튜플은 리스트처럼 다양한 자료형의 원소를 가지지만, 대괄호 대신 소괄호를 표시하며 원소를 변경할 수 없다. 
# 튜플은 다른 리스트나 내장함수도 원소로 가질 수 있음
myTuple = ('a', 'b', 'c', [10, 20, 30], abs, max)

# 인덱싱을 사용하여 4번째 원소인 리스트를 출력
print(myTuple[3])

# 5번째 원소인 내장함수 abs()에 -100을 파라미터로 전달
print(myTuple[4](-100))

# 6번째 원소인 내장함수 max()에 리스트를 파라미터로 전달
print(myTuple[5](myTuple[3]))

# 원소에 대한 변경이 정말 안 되는지 확인해보자. 첫 번째 원소에 'A'를 대입해 보자. '튜플 객체는 원소할당(item assignment)을 지원하지 않는다.'는 메세지와 함께 타입 에러가 발생할 것이다. 
myTuple[0] = 'A'