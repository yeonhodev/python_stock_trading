# Getting an image file by using request
import requests

url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream=True).raw