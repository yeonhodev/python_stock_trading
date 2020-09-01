# 함수를 정의할 때 반환값을 지정하지 않으면 None을 반환한다. 따라서 아래 세 함수는 모두 None을 반환한다. 참고로 다음처럼 세미콜론;을 사용하면 여러 줄 명령을 한 줄에 작성해 실행할 수 있다. 

def func1():
    pass

def func2():
    return

def func3():
    return None

print(func1()); print(func2()); print(func3())

# None은 NoneType 클래스의 객체이며, None이 반환되었는지 확인하려면 == 또는 is 연산자를 사용한다. 

print(type(None))
print(func1() == None)
print(func1() is None)