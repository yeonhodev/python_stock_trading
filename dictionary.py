# 최근 유전자 가위 기술(CRISPR)로 각광을 받는 미국 대표 기업들을 딕셔너리로 나타내면 다음과 같다. 
crispr = {'EDIT': 'Editas Medicine', 'NTLA': 'Intellia Therapeutics'}

# 순서가 없으므로 시퀀스 자료형들처럼 인덱스로 값에 접근하는 것은 불가능하다. 만일 다음처럼 인덱스 숫자로 원소에 접근하려고 하면, 인터프리터는 이를 키로 처리하기 때문에 키 에러가 발생한다. 

# print(crispr[1]) # 순서가 없으므로 인덱스 숫자로 접근할 수 없다. 

print(crispr['NTLA'])

# 원소를 추가하고 싶다면, 다음과 같이 키와 값을 함께 지정하여야 한다. 다음은 CRSP 키에 'CRISPR Therapeutics'를 값으로 넣는 예제다. 
crispr['CRSP'] = 'CRISPR Therapeutics'
print(crispr)

# CRSP 종목을 추가했으므로 총 원소 개수는 3개다. 
print(len(crispr))