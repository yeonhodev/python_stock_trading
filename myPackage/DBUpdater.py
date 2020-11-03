class DBUpdater:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
    
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