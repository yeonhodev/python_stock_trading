import ctypes
import win32com.client
from slacker import Slacker
from datetime import datetime
import slack_config

# CREON Plus 공동 Object
cpStatus = win32com.client.Dispatch('CpUtil.CpCybos')      # 시스템 상태 정보
cpTradeUtil = win32com.client.Dispatch('CpTrade.CpTdUtil')  # 주문 관련 도구

# CREON Plus 시스템 점검 함수
def check_creon_system():
    # 관리자 권한으로 프로세스 실행 여부
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('check_creon_system() : admin user -> FAILED')
        return False
    
    # 연결 여부 체크
    if (cpStatus.IsConnect == 0):
        print('check_creon_system() : connect to server -> FAILED')
        return False
    
    # 주문 관련 초기화
    if (cpTradeUtil.TradeInit(0) != 0):
        print('check_creon_system() : init trade -> FAILED')
        return False
    
    return True

slack_token = slack_config.token
# 7장 장고 웹 서버 구축 및 자동화에서 발급한 토큰을 입력한다. 
slack = Slacker(slack_token)
def dbgout(message):
    # datetime.now() 함수로 현재 시간을 구한 후 [월/일 시:분:초] 형식으로 출력한 후 한 칸 띄우고 함수 호출 시 인수로 받은 message 문자열을 출력한다. 
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)
    strbuf = datetime.now().strftime('[%m/%d %H:%M:%S]') + message
    # etf-algo-trading 채널로 메세지를 보내려면 워크스페이스에 etf-algo-trading 채널을 미리 만들어 둬야 한다. 별도의 채널을 만들기 싫다면 #etf-algo-trading 대신 #general을 인수로 주어 일반 채널로 메시지를 보내도 된다. 
    slack.chat.post_message('#etf-algo-trading', strbuf)

cpStock = win32com.client.Dispatch("DsCbo1.StockMst") # 주식 종목별 정보

def get_current_price(code):
    cpStock.SetInputValue(0, code) # 종목코드에 대한 가격 정보
    cpStock.BlockRequest()

    item = {}
    item['cur_price'] = cpStock.GetHeaderValue(11) # 현재가
    item['ask'] = cpStock.GetHeaderValue(16) # 매수호가
    item['bid'] = cpStock.GetHeaderValue(17) # 매도호가

    return item['cur_price'], item['ask'], item['bid']