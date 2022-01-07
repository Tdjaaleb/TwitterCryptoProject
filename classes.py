import pandas as pd
import numpy as np

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates
from mplfinance.original_flavor import candlestick_ohlc

from binance.client import Client

#====================TWEET====================
class Tweet :
    #==========INIT==========
    def __init__(self, id, author, text, date, type='tweet') : 
        self.id = id
        self.author = author
        self.text = text 
        self.date = date
        self.type = type
        self.candles = pd.DataFrame()
        self.priceInf = 0
        self.volumeInf = 0

    #==========STR==========
    def __str__(self):
        return'<id> '+str(self.id)+' <Tweet> '+self.text+' <Date> '+str(self.date)+' <Type> '+self.type

    #==========GET_KLINES==========
    def get_klines(self, params):
        client_bi=Client()
        Symbol = params["symbol"]
        Currency = params["currency"]
        Interval = params["interval"]
        symbol=Symbol+Currency
        tweet_time = self.date
        if Interval=='1':
            interval=Client.KLINE_INTERVAL_1MINUTE
            delta=3601000
            lim=120
        else:
            interval=Client.KLINE_INTERVAL_1HOUR
            delta=86401000
            lim=48
        klines = client_bi.get_historical_klines(
            symbol= symbol, 
            interval= interval, 
            start_str= int(datetime.timestamp(tweet_time)*1000-delta), 
            end_str= int(datetime.timestamp(tweet_time)*1000+delta),
            limit= lim
        )
        p_time=[]
        p_open=[]
        p_high=[]
        p_low=[]
        p_close=[]
        p_volume=[]
        for i in range(len(klines)):
            p_time.append(klines[i][0]/1000)
            p_open.append(klines[i][1])
            p_high.append(klines[i][2])
            p_low.append(klines[i][3])
            p_close.append(klines[i][4])
            p_volume.append(klines[i][5])
        df = {"Date" : p_time, "Open" : p_open, "High" : p_high, "Low" : p_low, "Close" : p_close, "Volume" : p_volume}
        self.candles = pd.DataFrame(df)
        self.candles=self.candles.astype("float64")

    #==========GET_INFLUENCE==========
    def get_influence(self, params):
        Interval=params["interval"]
        if Interval=='1':
            mid_ind=60
            last_ind=119
        else:
            mid_ind=24
            last_ind=47
        x=0
        y=0
        if self.candles.shape[0]==last_ind+1:
            for j in range(mid_ind) : 
                x = x + self.candles["Volume"][j]
                y = y + self.candles["Volume"][j+mid_ind]
            self.volumeInf = ((y/x)-1)*100
            var_c_brut = self.candles["Close"][last_ind] - self.candles["Open"][mid_ind]
            self.priceInf = (var_c_brut/self.candles["Open"][mid_ind])*100
        else:
            self.volumeInf=np.NaN
            self.priceInf=np.NaN

    #==========DRAW==========
    def draw(self, params):
        Symbol = params["symbol"]
        Interval = params["interval"] 
        Username = params["user"]
        tweet_time = self.date
        if Interval=='1':
            mid_ind=60
            last_ind=119
            start_arrow=65
            stop_arrow=115
            title="Movement 1hour before and after the tweet on "+Symbol
        else:
            mid_ind=24
            last_ind=47
            start_arrow=26
            stop_arrow=46
            title="Movement 1day before and after the tweet on "+Symbol
        plt.figure(figsize=(8,6), dpi=125)
        ax1 = plt.subplot2grid((1,1),(0,0))
        plt.axvline(
                x=datetime.timestamp(tweet_time),
                color='blue',
                lw=0.5
        )
        plt.figtext(x=0,y=1,s="Tweet : "+self.text)
        plt.figtext(x=0,y=0.95,s="Type : "+self.type)
        plt.title(title)
        if self.priceInf<0:
            col="red"
            movement=str(round(self.priceInf,2))+' %'
            y_arrow=round(self.candles["High"][mid_ind:last_ind].max(),3)
            dy_arrow=round(self.candles["High"][last_ind]-self.candles["High"][mid_ind:last_ind].max(),3)
            y_fig=0.8
        else:
            col="green"
            movement='+'+str(round(self.priceInf,2))+' %'
            y_arrow=round(self.candles["Low"][mid_ind:last_ind].min(),3)
            dy_arrow=round(self.candles["Low"][last_ind]-self.candles["Low"][mid_ind:last_ind].min(),3)
            y_fig=0.2
        plt.arrow(
            x=self.candles["Date"][start_arrow],
            y=y_arrow,
            dx=self.candles["Date"][stop_arrow]-self.candles["Date"][start_arrow],
            dy=dy_arrow,
            color=col,
            width= (self.candles["High"][0:last_ind].max()-self.candles["Low"][0:last_ind].min())/100
        )
        plt.figtext(x=0.8, y=y_fig, s=movement, color=col)
        plt.legend([Username+" tweet the "+str(self.date)])
        candlestick_ohlc(ax=ax1,quotes=self.candles.values, width=0.4, colordown="#db3f3f",colorup="#77d879")

#====================RESPONSETWEET====================
class ResponseTweet(Tweet):
    #==========INIT==========
    def __init__(self, tweet, answeringTo=''):
        self.id=tweet.id
        self.author = tweet.author
        self.text = tweet.text
        self.date = tweet.date
        self.answeringTo=answeringTo
        self.type='response'
    
    #==========STR==========
    def __str__(self):
        return'<id> '+str(self.id)+' <Tweet> '+self.text+' <Date> '+str(self.date)+' <Type> '+self.type+' <Answering to> '+self.answeringTo

#====================RETWEET====================
class Retweet(Tweet):
    #==========INIT==========
    def __init__(self, tweet, original_author=''):
        self.id=tweet.id
        self.author = tweet.author
        self.text = tweet.text
        self.date = tweet.date
        self.original_author=original_author
        self.type='response'
    
    #==========STR==========
    def __str__(self):
        return'<id> '+str(self.id)+' <Tweet> '+self.text+' <Date> '+str(self.date)+' <Type> '+self.type+' <Original Author> '+self.original_author


#====================TWITTOS====================
class Twittos:
    #==========INIT==========
    def __init__(self,user_id,username,Crypto):
        self.user_id =user_id
        self.username = username
        self.Crypto = Crypto
        self.NbTweet = 0
        self.Tweets = []
        self.priceInf = 0
        self.volumeInf = 0

    #==========STR==========
    def __str__(self):
        return "<id> "+str(self.user_id)+" <username> "+self.username+" <NbTweet> "+str(self.NbTweet)+" <Subject> "+self.Crypto
    
    #==========AFFICHER_TWEETS==========
    def Afficher_Tweets(self, type='all'):
        if type=='all':
            for i in enumerate(self.Tweets):
                print(i[1])
        else:
            for i in enumerate(self.Tweets):
                if i[1].type==type:
                    print(i[1])

    #==========ADD==========
    def add(self, Tweet):
        self.NbTweet+=1
        self.Tweets.append(Tweet)
    
    #==========REMOVE_DUPLICATES==========
    def remove_duplicates(self):
        ids=[]
        for i,tweet in enumerate(self.Tweets):
            ids.append(tweet.id)
        stop = len(ids)-2
        for i in range(len(ids)-1):
            if ids[i]==ids[i+1]:
                self.Tweets.remove(self.Tweets[i])
                ids.remove(ids[i])
                stop=stop-1
                self.NbTweet-=1
            if i==stop:
                break
    
    #==========GET_INFLUENCE==========
    def get_influence(self, params):
        Interval = params["interval"]
        Username = params["user"]
        price=[]
        volume=[]
        for i in enumerate(self.Tweets):
            price.append(i[1].priceInf)
            volume.append(i[1].volumeInf)
        self.priceInf=np.nanmean(price)
        self.volumeInf=np.nanmean(volume)
        print ('La moyenne des variations du cours sur '+Interval+'h est de', f'{self.priceInf:.3f}','%, après un tweet de '+Username)
        print ('La moyenne des variations des volumes sur '+Interval+'h est de', f'{self.volumeInf:.3f}','%, après un tweet de '+Username)

    #==========DRAW==========
    def draw(self, params):
        client_bi = Client()
        Username = params["user"]
        Symbol = params["symbol"]
        Currency = params["currency"]

        histKlines = client_bi.get_klines(
            symbol = Symbol+Currency,
            interval = Client.KLINE_INTERVAL_1DAY,
            limit = 1000
        )

        p_time=[]
        p_open=[]
        p_high=[]
        p_low=[]
        p_close=[]
        for i in range(len(histKlines)):
            p_time.append(matplotlib.dates.date2num(datetime.fromtimestamp(histKlines[i][0]/1000).date()))
            p_open.append(histKlines[i][1])
            p_high.append(histKlines[i][2])
            p_low.append(histKlines[i][3])
            p_close.append(histKlines[i][4])
        df = {"Date" : p_time, "Open" : p_open, "High" : p_high, "Low" : p_low, "Close" : p_close}
        df = pd.DataFrame(df)
        df=df.astype("float64")
        
        plt.figure(figsize=(8,6), dpi=125)
        ax1 = plt.subplot2grid((1,1),(0,0))
        for i in range(len(self.Tweets)):
            plt.axvline(
                x=matplotlib.dates.date2num(self.Tweets[i].date),
                color='blue',
                lw=0.5
            )
        candlestick_ohlc(ax=ax1,quotes=df.values, width=0.4, colordown="#db3f3f",colorup="#77d879")
        ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %y"))
        plt.title("Historical Daily "+Symbol+" vs "+Currency)
        plt.legend([Username+"'s tweets"])
        plt.ylabel=Currency

    #==========PLOT_TWEET==========
    def Plot_Tweet(self, params, id):
        x=0
        for i, tweet in enumerate(self.Tweets):
            if tweet.id==id:
                tweet.draw(params)
                x=1
        if x==0:
            print("L'id n'est pas bon")
