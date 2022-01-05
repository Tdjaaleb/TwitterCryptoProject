from binance.client import Client
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc

class Tweet : 
    def __init__(self, id, author, text, date, typeoftweet = 'tweet', answeringTo = '') : 
        self.id = id
        self.author = author
        self.text = text 
        self.date = date
        self.type = typeoftweet
        self.answeringTo = answeringTo
       
    def __str__(self):
        if self.answeringTo!='':
            return '<id> : '+str(self.id)+' <Tweet> : '+self.text+' <Date> : '+str(self.date)+' <Type> : '+self.type+' <Réponse à> : '+self.answeringTo 
        else:
            return'<id> : '+str(self.id)+' <Tweet> : '+self.text+' <Date> : '+str(self.date)+' <Type> : '+self.type
    
    def draw(self, params):
        client_bi=Client()

        Symbol = params["symbol"]
        Currency = params["currency"]
        Username = params["user"]
        Interval = params["interval"]
        symbol=Symbol+Currency
        tweet_time = self.date

        if Interval=='1':
            candles = client_bi.get_historical_klines(
                symbol= symbol, 
                interval= Client.KLINE_INTERVAL_1MINUTE, 
                start_str= int(datetime.timestamp(tweet_time)*1000-3601000), 
                end_str= int(datetime.timestamp(tweet_time)*1000+3601000),
                limit= 120 
            )
            x = 0 
            y = 0
            for j in range(60):
                x = x + float(candles[j][5])
                y = y + float(candles[j+60][5])
            var_v = ((y/x)-1)*100
            var_c_brut = float(candles[119][4]) - float(candles[60][1])
            var_c = (var_c_brut/float(candles[60][1]))*100
        else:
            candles = client_bi.get_historical_klines(
                symbol = symbol, 
                interval = Client.KLINE_INTERVAL_1HOUR, 
                start_str = int(datetime.timestamp(tweet_time)*1000-86401000), 
                end_str = int(datetime.timestamp(tweet_time)*1000+86401000),
                limit = 48 
            )
            x = 0 
            y = 0
            for j in range(24) : 
                x = x + float(candles[j][5])
                y = y + float(candles[j+24][5])
            var_v = ((y/x)-1)*100
            var_c_brut = float(candles[47][4]) - float(candles[24][1])
            var_c = (var_c_brut/float(candles[24][1]))*100

        p_time=[]
        p_open=[]
        p_high=[]
        p_low=[]
        p_close=[]
        for i in range(len(candles)):
            p_time.append(candles[i][0]/1000)
            p_open.append(candles[i][1])
            p_high.append(candles[i][2])
            p_low.append(candles[i][3])
            p_close.append(candles[i][4])
        df = {
            "Date" : p_time,
            "Open" : p_open,
            "High" : p_high,
            "Low" : p_low,
            "Close" : p_close
        }
        df = pd.DataFrame(df)
        df=df.astype("float64")
  
        plt.figure(figsize=(8,6), dpi=125)
        ax1 = plt.subplot2grid((1,1),(0,0))
        plt.axvline(
            x=datetime.timestamp(tweet_time),
            color='blue',
            lw=0.5
        )
        plt.figtext(x=0,y=1,s="Tweet : "+self.text)
        plt.figtext(x=0,y=0.95,s="Type : "+self.type)
        
        if Interval=='1':
            plt.title("Movement 1hour before and after the tweet on "+Symbol)
            if var_c<0:
                plt.arrow(
                    x=df["Date"][65],
                    y=round(df["High"][60:119].max(),3),
                    dx=df["Date"][115]-df["Date"][65],
                    dy=round(df["High"][119]-df["High"][60:119].max(),3),
                    color='red', 
                    #width=0.4
                )
                plt.figtext(
                    x=0.8,
                    y=0.8,
                    s=str(round(var_c,2))+' %',
                    color='red'
                )
            else:
                plt.arrow(
                    x=df["Date"][65],
                    y=round(df["Low"][60:119].min(),3),
                    dx=df["Date"][115]-df["Date"][65],
                    dy=round(df["Low"][119]-df["Low"][60:119].min(),3),
                    color='green',
                    #width=0.4
                )
                plt.figtext(
                    x=0.8,
                    y=0.2,
                    s='+'+str(round(var_c,2))+' %',
                    color='green'
                ) 
        else:
            plt.title("Movement 1day before and after the tweet on "+Symbol)
            if var_c<0:
                plt.arrow(
                    x=df["Date"][26],
                    y=round(df["High"][24:47].max(),3),
                    dx=df["Date"][46]-df["Date"][24],
                    dy=round(df["High"][47]-df["High"][24:47].max(),3),
                    color='red',
                    #width=0.4
                )
                plt.figtext(
                    x=0.8,
                    y=0.8,
                    s=str(round(var_c,2))+' %',
                    color='red'
                )
            else:
                plt.arrow(
                    x=df["Date"][26],
                    y=round(df["Low"][24:47].min(),3),
                    dx=df["Date"][46]-df["Date"][24],
                    dy=round(df["Low"][47]-df["Low"][24:47].min(),3),
                    color='green',
                    #width=0.4
                )
                plt.figtext(
                    x=0.8,
                    y=0.2,
                    s='+'+str(round(var_c,2))+' %',
                    color='green'
                )
        #plt.ylabel(Currency)
        plt.legend([Username+" tweet the "+str(self.date)])
        candlestick_ohlc(ax=ax1,quotes=df.values, width=0.4, colordown="#db3f3f",colorup="#77d879")
