# 데이터프레임 생성
import pandas as pd
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 24467, 2041], 'KOSDAQ': [542, 682, 631, 798, 675]})
print(df)

# 인덱스 추가
import pandas as pd
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 24467, 2041], 'KOSDAQ': [542, 682, 631, 798, 675]}, index=[2014, 2015, 2016, 2017, 2018])
print(df)

# 데이터프레임 객체에 포함된 데이터의 전체적 모습 확인
print(df.describe())

# 데이터프레임의 인덱스 정보, 칼럼 정보, 메모리 사용량 등을 확인
print(df.info())