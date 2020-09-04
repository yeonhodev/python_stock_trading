# 파이썬 모듈은 변수, 함수, 클래스를 포함할 수 있으며, import 예약어를 사용해 다른 모듈에 정의된 변수, 함수, 클래스 등을 자유롭게 불러와서 사용할 수 있다. 
# import 모듈명
# import 패키지명.모듈명
# 다음은 keyword 모듈을 import하여 파이썬 예약어를 확인하는 예제다. 물론 kwlist의 자료형은 리스타다. 

import keyword
print(keyword.kwlist)
print()

# import한 모듈이나 패키지의 실제 파일 위치를 알아보려며, __file__문자열 속성을 확인하면 된다. 
print(keyword.__file__)

# from 예약어를 사용하면, 실제 과정에서 from 다음에 지정한 패키지명이나 모듈명을 생략할 수 있다는 장점이 있다. 
# from 모듈명 import 클래스명, 함수명 등
# from 패키지명 import 모듈명

# 'import 모듈명' 형식으로 calendar 모듈을 임포트 한 경우, calendar 모듈 내의 month() 메서드를 호출하려면 다음 예제의 calendar.month()처럼 모듈명을 먼저 적어주어야 한다.

import calendar
print(calendar.month(2020, 1)) # 모듈명(calendar) 생략 불가

# 하지만 'from 모듈명 import 메서드명' 형식으로 임포트한 경우에는 다음처럼 모듈명 없이 메서드명을 바로 사용할 수 있다. 

from calendar import month
print(month(2020, 2)) # 모듈명(calendar) 생략 가능

# import ~ as ~ 
# as 예약어를 사용하면 이름이 긴 모듈명을 프로그래머가 원하는 별칭(alias)으로 줄여서 사용할 수 있다. 

# import 이름이_긴_모듈명 as 별칭
# from ~ import ~ as 별칭

import datetime
print(datetime.datetime.now()) # 별칭을 사용하지 않은경우

# datetime 모듈의 datetime 타입을 dt라는 별칭으로 지정하면, datetime.datetime.now()대신 dt.now()처럼 코드 길이를 짧게 줄일 수 있다. 
from datetime import datetime as dt
print(dt.now()) # 별칭(dt)를 사용한 경우