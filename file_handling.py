# Get an image file by using request
import requests

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw

# Show an image by using pillow
from PIL import Image

img = Image.open(r)
img.show()
img.save('src.png')