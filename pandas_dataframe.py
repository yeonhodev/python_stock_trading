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

# 시리즈를 이요한 데이터프레임 생성
kospi = pd.Series([1915, 1961, 2026, 2467, 2041], index=[2014, 2015, 2016, 2017, 2018], name='KOSPI')
print(kospi)
kosdaq = pd.Series([542, 682, 631, 798, 675], index=[2014, 2015, 2016, 2017, 2018], name='KOSDAQ')
print(kosdaq)
df = pd.DataFrame({kospi.name: kospi, kosdaq.name: kosdaq})
print(df)

# 리스트를 이용한 데이터프레임 생성
columns = ['KOSPI', 'KOSDAQ']
index = [2014, 2015, 2016, 2017, 2018]
rows = []
rows.append([1915, 542])
rows.append([1961, 682])
rows.append([2026, 631])
rows.append([2467, 798])
rows.append([2041, 675])
df = pd.DataFrame(rows, columns=columns, index=index)
print(df)