class Params:
    def __init__(self, username, symbol, currency, interval):
        self.user = username,
        self.symbol = symbol,
        self.currency = currency,
        self.interval = interval

class Tweet : 
    def __init__(self, id, author, text, date, typeoftweet = 'tweet', answeringTo = []) : 
        self.id = id
        self.author = author
        self.text = text 
        self.date = date
        self.type = typeoftweet
        self.answeringTo = answeringTo
       
    def __str__(self):
        
    def draw(self):
