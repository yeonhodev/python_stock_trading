# __name__ 속성
# 명령창에서 파이썬 셸을 이용하여 moduleA 모듈을 실행할 수 있다. 함수 정의를 제외한 나머지 부분이 실행되므로 print('MODULE_A :', __name__) 코드에 의해 'MODULE_A : __main__'이 출력된다. 

# moduleA 모듈을 직접 실행하지 않고, 파이썬 셸에서 임포트만 해도 print("MODULE_A :", __name__) 코드가 실행되면서 'MODULE_A : myPackage.moduleA'이 출력된다. 이처럼 __name__속성은 단독으로 실행될 때는 '__main__'문자열이 되고, 임포트할 때는 실제 모듈명('myPackage.moduleA')이 된다. 

