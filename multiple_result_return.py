# 파이썬은 함수 호출이 끝나고 결과값을 반환할 때, 여러 결과값을 한꺼번에 반환할 수 있다. 여거 결과값은 기본적으로 튜플 객체로 변환되어 반환된다. 

def myFunc():
    var1 = 'a'
    var2 = [1, 2, 3]
    var3 = max
    return var1, var2, var3 # 여러 개의 결과값은 기본적으로 튜플 타입으로 반환된다. 

print(myFunc())

# 함수 결과값을 튜플 객체 하나로 받지 않고, 함수에서 반환한 순서대로 여러 객체로 나누어 받으려면 변수를 쉼표로 구분하여 받으면 된다. 
s, l, f = myFunc()
print(s)
print(l)
print(f)