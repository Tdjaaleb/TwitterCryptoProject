class Tweet : 
    def __init__(self, id, author, text, date, typeoftweet = 'tweet', answeringTo = []) : 
        self.id = id
        self.author = author
        self.text = text 
        self.date = date
        self.type = typeoftweet
        self.answeringTo = answeringTo
       
    def print(self):
        print ('Tweet : ' + self.text)
        print ('Date : ' + self.date)
        print ('Type : ' + self.type)
        if (self.answeringTo!=[]) : 
            print ('Réponse à : ' + self.answeringTo)       
