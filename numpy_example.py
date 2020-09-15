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