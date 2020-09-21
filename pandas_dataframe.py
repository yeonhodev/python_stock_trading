# 데이터프레임 생성
import pandas as pd
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 24467, 2041], 'KOSDAQ': [542, 682, 631, 798, 675]})
print(df)

# 인덱스 추가
import pandas as pd
df = pd.DataFrame({'KOSPI': [1915, 1961, 2026, 24467, 2041], 'KOSDAQ': [542, 682, 631, 798, 675]}, index=[2014, 2015, 2016, 2017, 2018])
print(df)
