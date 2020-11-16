import pandas as pd
#from bs4 import BeautifulSoup
#import urllib
#from urllib.request import urlopen
import pymysql
#import time
#import pandas.io.sql as sql
from datetime import datetime
#from threading import Timer
#import matplotlib.pyplot as plt

class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', password='snake.land.', db='INVESTAR', charset='utf8')
        # dict()로 생성 가능하지만, 조금 더 파이썬답게 생성하고자 리터럴을 사용하여 생성했다. 
        self.codes = {}
        # get_com_info() 함수를 호출하여 마리아디비에서 company_info 테이블을 읽어와서 codes에 저장한다.
        self.get_comp_info()
        
    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def get_comp_info(self):
        """company_info 테이블에서 읽어와서 companyData와 codes에 저장"""
        sql = "SELECT * FROM company_info"
        companyInfo = pd.read_sql(sql, self.conn)
        for idx in range(len(companyInfo)):
            self.codes[companyInfo['code'].values[idx]] = companyInfo['company'].values[idx]

    def get_daily_price(self, code, start_date=None, end_date=None):
        """daily_price 테이블에서 읽어와서 데이터프레임으로 반환"""
        sql = f"SELECT * FROM daily_price WHERE code = '{code}' and date >= '{start_date}' and date <= '{end_date}'"
        # 팬더스의 read_sql() 함수를 이용해 SELECT 결과를 데이터프레임으로 가져오면 정수형 인덱스가 별도로 생성된다. 
        df = pd.read_sql(sql, self.conn)
        # 따라서 df.index = df['date']로 데이터프레임의 인덱스를 date 칼럼으로 새로 설정해야 한다. 
        df.index = df['date']
        return df



