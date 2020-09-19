import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)
print(type(A))
print(A.ndim) # 배열의 차원
print(A.shape) # 배열 크기
print(A.dtype) # 원소 자료형
print(A.max(), A.mean(), A.min(), A.sum())

# 배열의 접근
print(A[0]) # A 배열의 첫 번째 행
print(A[1]) # A 배열의 두 번째 행

# A 배열의 원소에 접근하는 데 A[행 인덱스][열 인덱스] 형식을 사용해도 되고, A[행 인덱스, 열 인덱스] 형식을 사용해도 된다. 
print(A[0][0], A[0][1])
print(A[1][0], A[1][1])
print(A[0, 0], A[0, 1])
print(A[1, 0], A[1, 1])

# 조건에 맞는 원소들만 인덱싱할 수도 있다. 
print(A[A>1])

# Transpose - 배열의 요소를 주대각선을 기준으로 뒤바꾸는 것
print(A)
print(A.T) # A.transpose()와 같다. 

# Flatten - 다차원 배열을 1차원 배열 형태로 바꾸는 것; 평탄화
print(A)
print(A.flatten())

# 배열의 연산 (Array Operations)
# 같은 크기의 행렬끼리는 사칙 연산을 할 수 있다. 두 행렬에서 같은 위치에 있는 원소끼리 연산을 하면 된다. 

print(A + A) # np.add(A, A)와 같다. 
print(A - A) # np.subtract(A, A)와 같다. 
print(A * A) # np.multiply(A, A)와 같다. 
print(A / A) # np.divide(A, A)와 같다. 

# Broadcasting ; 수학에서는 크기가 같은 행렬끼리만 연산을 할 수 있다. 하지만 넘파이에서는 행렬의 크기가 달라도 연산할 수 있게 크기가 작은 행렬을 확장해 주는데, 이를 브로드캐스팅이라고 한다. 다음은 B 행렬을 A 행렬의 크기에 맞게 브로드캐스팅하여 연산한 예이다. 

B = np.array([10, 100])
print(A * B)