import pymysql
import pandas as pd
import mariadb_config
from datetime import datetime

passwd = mariadb_config.passwd

class DBUpdater:
    # DBUpdater의 생성자 내부에서 마리아디비에 연결한다. 
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
    
    # KRX로 부터 상장법인 목록 파일을 읽어온다. 
    def read_krx_code(self):
        """KRX로 부터 상장법인목록 파일을 읽어와서 데이터프레임으로 변환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
        
        # 상장법인목록 .xls 파일을 read_html() 함수로 읽는다. 
        krx = pd.read_html(url, header=0)[0]

        # 종목코드 칼럼과 회사명만 남긴다. 데이터프레임에 [[]]을 사용하면 특정 칼럼만 뽑아서 원하는 순서대로 재구성할 수 있다. 
        krx = krx[['종목코드', '회사명']]

        # 한글 칼럼명을 영문 칼럼명으로 변경한다. 
        krx = krx.rename(columns={'종목코드':'code', '회사명':'company'})

        # 종목코드 형식을 {:06d} 형식의 문자열로 변경한다. 
        krx.code = krx.code.map('{:06d}'.format)
        
        return krx
    
    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트한 후 딕셔너리에 저장"""
        sql = "SELECT * FROM company_info"

        # company_info 테이블을 read_sql() 함수로 읽는다. 
        df = pd.read_sql(sql, self.conn)

        # 위에서 읽은 데이터프레임을 이용해서 종목코드와 회사명으로 codes 딕셔너리를 만든다.  
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]]=df['company'].values[idx]
        with self.conn.cursor() as curs:
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            # SELECT max() ~ 구문을 이용해서 DB에서 가장 최근 업데이트 날짜를 가져온다. 
            rs = curs.fetchone()
            today = datetime.today().strftime('%Y-%m-%d')

            # 위에서 구한 날짜가 존재하지 않거나 오늘보다 오래된 경우에만 업데이트 한다. 
            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today:
                # KRX 상장기업 목록 파일을 읽어서 krx 데이터프레임을 저장한다. 
                krx = self.read_krx_code()
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]
                    sql = f"REPLACE INTO company_info (code, company, last_update) VALUES ('{code}', '{company}', '{today}')"
                    # REPLACE INTO 구문을 이용해서 '종목코드, 회사명, 오늘날짜' 행을 DB에 저장한다. 
                    curs.execute(sql)
                    # codes 딕셔너리에 '키-값'으로 종목코드와 회사명을 추가한다. 
                    self.codes[code] = company
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] {idx:04d} REPLACE INTO company_info VALUES({code}, {company}, {today})")
                    self.conn.commit()
                    print()

    def read_naver(self, code, company, pages_to_fetch):
        """네이버 금융에서 주식 시세를 읽어서 데이터프레임으로 반환"""
        try:
            url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
            with urlopen(url) as doc:
                if doc is None:
                    return None
                html = BeautifulSoup(doc, 'lxml')
                pgrr = htmlfind("td", class_="pgRR")
                if pgrr is None:
                    return None
                s = str(pgrr.a["href"]).split('=')
                # 네이버 금융에서 일별 시세의 마지막 페이지를 구한다. 
                lastpage = s[-1]
            df = pd.DataFrame()
            # 설정 파일에 설정된 페이지 수 (pages_to_fetch)와 위에서 구한 일별시세의 마지막 페이지 중 작은 것을 선택한다. 
            pages = min(int(lastpage), pages_to_fetch)
            for page in range(1, pages + 1):
                pg_url = '{}&page={}'.format(url, page)
                # 일별 시세 페이지를 read_html()로 읽어서 데이터프레임에 추가한다. 
                df = df.append(pd.read_html(pg_url, header=0)[0])
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.format(tmnow, company, code, page, pages), end="\r")
            # 네이버 금융의 한글 칼럼명을 영문 칼럼명으로 변경한다. 
            df = df.rename(columns={'날짜':'date', '종가':'close', '전일비':'diff', '시가':'open', '고가':'high', '저가':'low', '거래량':'volume'})
            # 연.월.일 형식의 일자 데이터를 연-월-일 형식으로 변경한다. 
            df['date'] = df['date'].replace('.', '-')
            df = df.dropna()
            # 마리아디비에서 BIGINT 형으로 저장한 칼럼들의 데이터형을 int 형으로 변경한다. 
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close', 'diff', 'open', 'high', 'lose', 'volume']].astype(int)
            # 원하는 순서대로 칼럼을 재조합하여 데이터프레임을 만든다. 
            df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
        except Exception as e:
            print('Exception occured :', str(e))
            return None
        return df

    def replace_into_db(self, df, num, code, company):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""

    def execute_daily(self):
        """실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트"""
    
if __name__ == '__main__':
    # DBUpdater.py가 단독으로 실행되면 DBUpdater 객체를 생성한다. 
    dbu = DBUpdater()

    dbu.execute_daily()
    
    # company_info 테이블에 오늘 업데이트 된 내용이 있는지 확인하고, 없으면 read_krx_code()를 호출하여 company_info 테이블에 업데이트 하고 codes 딕셔너리에도 저장한다. 
    dbu.update_comp_info()