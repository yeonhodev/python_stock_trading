import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dst_img = mpimg.imread('dst.png')
print(dst_img)

pseudo_img = dst_img [:, :, 0] # RGB 채널 중 첫 번째 채널(0)만 슬라이싱해서 저장한 관계로 부동소수점 데이터가 2차원으로 변경되었다.
print(pseudo_img)