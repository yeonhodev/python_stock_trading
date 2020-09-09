"""
상속은 클래스가 가지는 모든 속성과 메서드를 다른 클래스에게 물려주는 기법이다. 
자식 클래스는 여러 부모 클래스로부터 상속 받을 수 있는데, 이를 다중 상속이라고 한다.
class 자식 클래스(부모 클래스 1, 부모 클래스 2, ...):
    pass
"""

class A:
    def methodA(self):
        print("Calling A's methodA")
    def method(self):
        print("Calling A's method")

class B:
    def methodB(self):
        print("Calling B's methdB")

class C(A, B):
    def methodC(self):
        print("Calling C's methodC")
    def method(self):
        print("Calling C's overridden method")
        # 부모의 변수나 메소드를 사용할 때는 super() 내장 함수를 호출하면 된다. 
        super().method()

c = C()
print(c.methodA())
print(c.methodB())
print(c.methodC())
print(c.method())

# 위 예제의 method() 메서드처럼 자식 클래스에서 부모 클래스의 메서드 이름과 인수 형식과 동일하게 매서드를 재정의 하는 것을 오버라이딩이라고 한다. 