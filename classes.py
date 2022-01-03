class Params:
    def __init__(self, username, symbol, currency, interval):
        self.user = username,
        self.symbol = symbol,
        self.currency = currency,
        self.interval = interval

class Tweet : 
    def __init__(self,ID, author , text , date , answeringTo=[]) : 
        self.id = ID
        self.author = author
        self.text = text 
        self.date = date 
        self.answeringTo = answeringTo 
        
    def draw(self) : 
        
