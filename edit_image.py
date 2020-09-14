import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dst_img = mpimg.imread('dst.png')
print(dst_img)

pseudo_img = dst_img [:, :, 0] # RGB 채널 중 첫 번째 채널(0)만 슬라이싱해서 저장한 관계로 부동소수점 데이터가 2차원으로 변경되었다.
print(pseudo_img)

# subplot() 함수로 두 이미지를 나란히 표시하자. 
plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1) # 인수를 1, 2, 1 처럼 쉼표로 구분해 넘겨주면 1행 2열의 행렬에서 첫 번째(1) 그림을 설정하는 것이다. 
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))

plt.subplot(122) # 인수를 쉼표 구분 없이 모두 붙여서 전달할 수도 있다. 예를 들어 1행 2열의 행렬에서 두 번째 그림을 설정할 때는 인수를 122처럼 숫자를 모두 붙여 넘겨줄 수도 있다. 

plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:, :, 0]
plt.imshow(pseudo_img)
plt.show()