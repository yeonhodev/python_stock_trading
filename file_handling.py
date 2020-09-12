# Get an image file by using request
import requests

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw

# Show an image by using pillow
from PIL import Image

img = Image.open(r)
img.show()
img.save('src.png')

# Print file info
print(img.get_format_mimetype)

# copy an image file with 'with ~ as'
BUF_SIZE = 1024
# 1. 원본 이미지 파일(scr.png)을 바이너리 읽기 모드로 열어서 sf 파일 객체를 생성하고, 대상 이미지 파일 (dst.png)을 바이너리 쓰기 모드로 열어서 df 파일 객체를 생성한다. 
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        # 2. sf 파일 객체로 부터 1024 바이트씩 읽는다. 
        data = sf.read(BUF_SIZE) 
        if not data:
            # 3. 읽을 data가 없다면 while 반복문을 빠져나온다.
            break
        # 4. 읽어 온 data를 df 파일 객체에 쓰고 2 부터 다시 반복한다. 
        df.write(data)

# SHA-256으로 파일 복사 검증하기
# 해시는 암호화폐 지갑의 주소처럼 긴 데이터 값을 입력받아서 고정 길이의 고유한 값으로 변환하는 것이 핵심 기능이다.
import hashlib
# 원본 이미지 파일과 사본 이미지 파일에 대한 해시 객체를 각각 생성한다. 
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

# 원본 이미지 파일(src.png)을 바이너리 읽기 모드(rb)로 열어서 sf 파일 객체를 생성하고, 사본 이미지 파일(dst.png)을 바이너리 읽기 모드(rb)로 열어서 df 파일 객체를 생성한다.
with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    # sf 파일 객체로부터 전체 내용을 읽어서 원본 이미니제 대한 해시 객체(sha_src)를 업데이트한다. df 파일 객체로부터 전체 내용을 읽어서 사본 이미지에 대한 해시 객체(sha_dst)를 업데이트한다. 
    sha_src.update(sf.read())
    sha_dst.update(df.read())

# 원본 이미지 파일과 사본 이미지 파일을 해시값을 16진수로 각각 출력한다. 
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))