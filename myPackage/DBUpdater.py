import pymysql
import mariadb_config

passwd = mariadb_config.passwd

class DBUpdater:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', password=passwd, db='INVESTAR', charset='utf8')

        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE, 
                PRIMARY KEY (code)
            )
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price(
                code VARCHAR(20), 
                date DATE, 
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20), 
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date)
            )
            """
            curs.execute(sql)
        self.conn.commit()

        self.codes = dict()

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()
    
    def read_krx_code(self):
        """KRX로 부터 상장법인목록 파일을 읽어와서 데이터프레임으로 변환"""
    
    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
    
    def read_naver(self, code, company, pages_to_fetch):
        """네이버 금융에서 주식 시세를 읽어서 데이터프레임으로 변환"""

    def replace_into_db(self, df, num, code, company):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""

    def execute_daily(self):
        """실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트"""
    
if __name__ == '__main__':
    dbu = DBUpdater()
    dbu.execute_daily()