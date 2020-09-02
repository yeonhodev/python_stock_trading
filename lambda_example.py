# lambda는 이름 없는 간단한 함수를 만들 때 사용한다. 'lambda 인수 : 표현식'형태로 사용하며, 아래에 선언된 함수 객체와 비슷하게 동작한다. 
"""
def lambda ( 인수 ):
    return 표현식
"""

# 람다로 천 단위 숫자에 쉼표 삽입해 보자. 
insertComma = lambda x : format(x, ',')
print(insertComma(1234567890))
