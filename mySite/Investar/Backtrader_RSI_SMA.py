import backtrader as bt
from datetime import datetime

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.rsi = bt.indicators.RSI_SMA(self.data.close, period=21)
    
    # 기존 코드에 비해서 가장 큰 변화는 MyStrategy 클래스에 notify_order() 메서드가 추가되었다는 점이다. 이 메서드는 주문(order) 상태에 변화가 있을 때마다 자동으로 실행된다. 인수로 주문(order)를 객체를 넘겨 받는다. 주문 상태는 완료(Completed). 취소(Cancelled) 
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        # 주문 상태가 완료(Completed)이면 매수인지 매도인지 확인하여 상세 주문 정보를 출력한다. 주문 처리 관련 코드는 기존과 같다. 단지 주문 상태를 출력해주는 기능을 추가했다. 
        if order.status in[order.Completed]:
            if order.isbuy():
                self.log(f'BUY : 주가 {order.executed.price:,.0f}, 수량 {order.executed.size:,.0f}, 수수료 {order.executed.comm:,.0f}, 자산 {cerebro.broker.getvalue():,.0f}')
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            else:
                self.log(f'SELL : 주가 {order.executed.price:,.0f}, 수량 {order.executed.size:,.0f}, 수수료 {order.executed.comm:,.0f}, 자산 {cerebro.broker.getvalue():,.0f}')
            self.bar_executed = len(self)
        elif order.status in [order.Cancelled]:
            self.log('ORDER CANCELLED')
        elif order.status in [order.Margin]:
            self.log('ORDER MARGIN')
        elif order.status in [order.Rejected]:
            self.log('ORDER REJECTED')
        self.order = None
    
    def next(self):
        if not self.position:
            if self.rsi < 30:
                self.order = self.buy()
        else:
            if self.rsi > 70:
                self.order = self.sell()

    # log() 메서드는 텍스트 메세지를 인수로 받아서 셀 화면에 주문 일자와 함께 출력하는 역할을 한다. 
    def log(self, txt, dt=None):
        dt = self.datas[0].datetime.date(0)
        print(f'[{dt.isoformat()}] {txt}')

cerebro = bt.Cerebro()
cerebro.addstrategy(MyStrategy)
data = bt.feeds.YahooFinanceData(dataname='036570.KS', fromdate=datetime(2017, 1, 1), todate=datetime(2019, 12, 1))
cerebro.adddata(data)
cerebro.broker.setcash(10000000)
# 수수료(commission)는 매수나 매도가 발생할 때마다 차감된다. 우리나라는 주식을 매도할 때 0.25%를 증권거래세로 내야 하고, 증권회사별로 다르긴 하지만 주식을 매수하거나 매도할 때 일반적으로 0.015%를 증권거래수수료로 내야 한다. 즉, 주식을 한 번 거래(매수/매도)할 때 대략 0.28% 비용이 소요된다. 백트레이더에서는 매수와 매도 시점마다 수수료가 동일 비율로 두 번 차감되므로, 0.28%를 2로 나누어 수수료를 0.14%로 설정했다. 
cerebro.broker.setcommission(commission=0.0014)
# 사이즈(size)는 매매 주문을 적용할 주식수를 나타내며, 특별히 지정하지 않으면 1이다. PercentSizer를 사용하면 포트폴리오 자산에 대한 퍼센트로 지정할 수 있는데, 100으로 지정하면 수수료를 낼 수 없어서 ORDER MARGIN이 발생하므로, 수수료를 차감한 퍼센트로 저장해야 한다. 
cerebro.addsizer(bt.sizers.PercentSizer, percents=90)

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()
print(f'Final Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
# 주가를 표시할 때 캔들스틱 차트로 표시한다. 
cerebro.plot(style='candlestick')
