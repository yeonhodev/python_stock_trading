# 패키지는 여러 모듈(.py 파일)을 특정 디렉터리에 모아놓은 것이다. 패키지명 뒤에 '.'를 붙이고 모듈명을 사용할 수 있다. 예를 들어 A.B로 표기하면 A 패키지의 하위 모듈 B를 명시한 것이다. 이렇게 사용하면 여러 모듈을 사용할 때 모듈명이나 전역변수가 겹치는 문제를 피할 수 있다. 다음은 urllib 패키지의 request 모듈의 자료형을 type() 함수로 확인한 예이다. 

import urllib.request
print(type(urllib.request)) # urllib.request 모듈의 타입은 module이다. 

import urllib
print(type(urllib)) # urllib의 타입은 module로 표시된다. 
print(urllib.__path__) # urllib은 __path__ 속성이 있으므로 패키지다. 
print(urllib.__package__) # urllib이 속한 패키지는 urllib이다. 