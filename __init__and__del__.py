class NasdaqStock:
    """Class for NASDAQ stocks""" # 독스트링
    count = 0 # 클래스 변수
    def __init__(self, symbol, price):
        """Constructor for NasdaqStock""" # 독스트링
        self.symbol = symbol # 인스턴스 변수
        self.price = price # 인스턴스 변수
        NasdaqStock.count += 1
        print('Calling __init__({}, {:2f}) > count: {}'.format(self.symbol, self.price, NasdaqStock.count))
    
    def __del__(self):
        """Destructor for NasdaqStock""" # 독스트링
        print("Calling __del__({})".format(self))
    
gg = NasdaqStock("GOOG", 1154.05)
del(gg)
ms = NasdaqStock("MSFT", 102.44)
del(ms)
amz = NasdaqStock("AMZN", 1764.00)
del(amz)