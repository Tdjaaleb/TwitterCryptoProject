class Params:
    def __init__(self, username, symbol, currency, interval):
        self.user = username,
        self.symbol = symbol,
        self.currency = currency,
        self.interval = interval

class Tweet : 
    def __init__(self,ID, author , text , date , symbol, answeringTo=[]) : 
        self.id = ID
        self.author = author
        self.text = text 
        self.date = date 
        self.symbol = symbol.upper() + 'USDT'
        self.answeringTo = answeringTo 
        
