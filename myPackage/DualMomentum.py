import mariadb_config

passwd = mariadb_config.passwd

class DualMomentum:
    def __init__(self):
        """생성자: KRX 종목코드(codes)를 구하기 위한 MarketDB 객체 생성"""
        self.mk = Analyzer.MarketDB()

    def get_rltv_momentum(self, start_date, end_date, stock_count):
        """특정 기간 동안 수익률이 제일 높았던 stock_count 개의 종목들 (상대 모멘텀)
            - start_date    : 상대 모멘텀을 구할 시작일자 ('2020-01-10')
            - end_date      : 상대 모멘텀을 구할 종료일자 ('2020-12-31')
            - stock_count   : 상대 모멘텀을 구할 종목수
        """
        connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR', user='root', passwd=passwd, autocommit=True)
        cursor = connection.cursor()

        sql = f"SELECT MAX(date) FROM daily_price WHERE date <= '{start_date}'"
        # daily_price 테이블에서 사용자가 입력한 일자와 같거나 작은 일자를 조회함으로써 실재 거래일을 구한다. 
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[0] is None):
            print("start_date : {} -> returned None".format(sql))
            return
        # DB에서 조회된 거래일을 %Y-%m-%d 포맷 문자열로 변환해 사용자가 입력한 조회 시작 일자 변수에 반영한다. 
        start_date = result[0].strftime('%Y-%m-%d')

        sql = f"SELECT MAX(date) FROM daily_price WHERE date <= '{end_date}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[0] is None):
            print("end_date : {} -> returned None".format(sql))
            return
        end_date = result[0].strftime('%Y-%m-%d')

        return df
    
    def get_abs_momentum(self, rltv_momentum, start_date, end_date):
        """특정 기간 동안 모멘텀에 투자했을 때의 평균 수익률 (절대 모멘텀)
            - rltv_momentum : get_rltv_momentum() 함수의 리턴값 (상대 모멘텀)
            - start_date    : 절대 모멘텀을 구할 매수일 ('2020-01-01')
            - end_date      : 절대 모멘텀을 구할 매도일 ('2020-12-31')
        """
        return