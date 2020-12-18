from django.shortcuts import render
from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_data(symbol):
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc, "lxml", from_encoding='euc-kr')
        # id가 '_nowVal'인 <strong> 태그를 찾는다. cur_price 변수에 <strong class="tahp11" id="_nowVal">172,000</strong>태그가 저장된다. 
        cur_price = soup.find('strong', id='_nowVal')
        # id가 '_rate'인 <strong> 태그를 찾는다. cur_rate 변수에 <strong id="_rate"><span class="tah p11 nv01">-0.58%</span></strong>태그가 가 저장된다.
        cur_rate = soup.find('strong', id='_rate')
        # <title> 태그를 찾는다. stock 변수에 <title>NAVER : 네이버 금융</title> 태그가 저장된다. 
        stock = soup.find('title')
        # <title> 태그에서 콜론 (':') 문자를 기준으로 문자열을 분리하여 종목명을 구한 뒤 문자 열 좌우의 공백문자를 제거한다. 
        stock_name = stock.text.split(':')[0].strip()
        return cur_price.text, cur_rate.text.strip(), stock_name