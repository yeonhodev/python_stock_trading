# 시리즈 생성
import pandas as pd
s = pd.Series([0.0, 3.6, 2.0, 5.8, 4.2, 8.0]) # 리스트로 시리즈 생성
print(s)

# 시리즈의 인덱스 변경
s.index = pd.Index([0.0, 1.2, 1.8, 3.0, 3.6, 4.8]) # 인덱스 변경
s.index.name = 'MY_IDX' # 인덱스명 설정
print(s)

s.name = 'MY_SERIES' # 시리즈명 설정
print(s)

# 데이터 추가
s[5.9] = 5.5
print(s)

ser = pd.Series([6.7, 4.2], index=[6.8, 8.0]) # ser 시리즈 생성
s = s.append(ser) # 기존 s 시리즈에 신규 ser 시리즈를 추가
print(s)

# 데이터 인덱싱
print(s.index[-1]) # -1은 제일 마지막을 의미하므로 제일 마지막 인덱스 값을 출력
print(s.values[-1]) # 인덱스 순서에 해당하는 데이터를 구하려면 values 속성을 사용한다. 
print(s.loc[8.0]) # 인덱스를 이용해서 실제로 가리키는 작업을 수행하는 인덱서를 사용해서 데이터를 표시할 수도 있다. 인덱스값을 사용하는 loc 인덱서와 정수 순서를 사용하는 iloc 인덱서가 있다. 
print(s.loc[8.0]) # 로케이션 인덱서
print(s.iloc[-1]) # 인티저 로케이션 인덱서

# iloc와 values는 인덱스 순서에 해당하는 데이터를 술력한다는 점에서 동일하지만, values는 결과값이 복수개 일 때 배열로 반환하고, iloc는 시리즈로 반환하는 차이점이 있다. 
print(s.values[:])
print(s.iloc[:])

# 데이터 삭제
s = s.drop(8.0) # s.drop(s.index[-1])과 같다. s 시리즈에 변화를 주지 않으려면 대입하지 않으면 됨
print(s)

# 시리즈 정보 보기
print(s.describe())