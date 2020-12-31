# BlockRequest() 함수를 사용해서 삼성전자(종목코드 005930)의 현재가와 전일대비 가격을 구하는 예는 다음과 같다. 
import win32com.client

# 주식마스터(StockMst) COM 객체를 생성한다. 
obj = win32com.client.Dispatch("DsCbo1.stockMst")
# SetInputValue() 함수로 조회할 데이터를 삼성전자로 지정한다. 
obj.SetInputValue(0, 'A005930')
# BlockRequest() 함수로 삼성전자에 대한 블록 데이터를 요청한다. 
obj.BlockRequest()
sec = {}
# GetHeaderValue() 함수로 현재가 정보(11)를 가져와서 sec 딕셔너리에 넣는다. 
sec['현재가'] = obj.GetHeaderValue(11)
# GetHeaderValue() 함수로 전일대비 가격변동 정보(12)를 가져와서 sec 딕셔너리에 넣는다. 
sec['전일대비'] = obj.GetHeaderValue(12)
