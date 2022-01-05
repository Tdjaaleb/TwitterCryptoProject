#===============FONCTION QUI RECUPERE ET TRI LES TWEETS QUI NOUS INTERESSENT===============
import tweepy
from datetime import datetime
from cryptoDict import CryptoDict
from API_KEY import key,secret,access,access_s,bearer
from classes import Tweet

def Get_Relevant_Tweets(params):
  Username = params["user"]
  Symbol = params["symbol"]

  client_twi = tweepy.Client(
    bearer_token = bearer,
    consumer_key = key,
    consumer_secret = secret,
    access_token = access,
    access_token_secret = access_s
  )
  liste=[]
  user = client_twi.get_user(
    username = Username,
    user_fields = 'public_metrics'
  ) #Récupère les informations de l'utilisateur en fonction de son nom d'utilisateur

  if user.data==None:
    print("L'utilisateur n'existe pas")
    return(None)

  user_id = user.data["id"] #Id utilisateur
  iter_max = int(user.data.public_metrics["tweet_count"]/100)+1 #Nb de tweets divisé par 100 pour créer la boucle
  
  timer = str(datetime.utcnow())
  timer = timer.replace(' ','T')
  timer = timer.split('.')[0]+'Z'
  
  for i in range(iter_max):
    Tweets = client_twi.get_users_tweets(
        id=user_id,
        max_results=100,
        tweet_fields='created_at',
        end_time=timer
    )
    if type(Tweets.data)==list:
      for j in enumerate(Tweets.data):
        for k in enumerate(CryptoDict[Symbol]):
          if j[1].text.lower().find(k[1])!=-1:
            if j[1].text.find('@')==0:
              tweet_type = 'response'
              answering = j[1].text.split('@')[1]
              answering = answering.split(' ')[0]
              x = Tweet(
                id = Tweets.data[j[0]]["id"],
                author = Username,
                text = Tweets.data[j[0]]["text"],
                date = Tweets.data[j[0]].created_at,
                typeoftweet = tweet_type,
                answeringTo = answering
              )
            elif j[1].text.lower().find('rt')==0:
              tweet_type = 'retweet'
              x = Tweet(
                id = Tweets.data[j[0]]["id"],
                author = Username,
                text = Tweets.data[j[0]]["text"],
                date = Tweets.data[j[0]].created_at,
                typeoftweet = tweet_type
              )
            else:
              x = Tweet(
                id = Tweets.data[j[0]]["id"],
                author = Username,
                text = Tweets.data[j[0]]["text"],
                date = Tweets.data[j[0]].created_at
              )
            liste.append(x)
        timer = str(Tweets.data[j[0]].created_at)
        timer = timer.replace(' ','T')
        timer = timer.split('+')[0]+'Z'
  return(liste)

#===============FONCTION QUI PERMET DE TRACER L'HISTORIQUE DE LA CRYPTOMONNAIE EN AJOUTANT LES TWEETS===============
import pandas as pd
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates
from binance.client import Client

def Plot_Historical(listeTweets, params):
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
  for i in range(len(listeTweets)):
    plt.axvline(
      x=matplotlib.dates.date2num(listeTweets[i].date),
      color='blue',
      lw=0.5
    )
  candlestick_ohlc(ax=ax1,quotes=df.values, width=0.4, colordown="#db3f3f",colorup="#77d879")
  ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%b %y"))
  plt.title("Historical Daily "+Symbol+" vs "+Currency)
  plt.legend([Username+"'s tweets"])
  plt.ylabel=Currency


#===============FONCTION QUI ANALYSE LES MOUVEMENTS DU MARCHES APRES LES TWEETS===============
from binance.client import Client
from datetime import datetime
import pandas as pd
import numpy as np

def MarketAnalysis(listeTweets, params):
  client_bi=Client()

  Symbol = params["symbol"]
  Currency = params["currency"]
  Username = params["user"]
  Interval = params["interval"]

  symbol=Symbol+Currency

  data = pd.DataFrame(columns=['Tweet','Date','Variation du cours (en %)', 'Variation du volume (en %)'])

  if (Interval == '1'): 
    for i in range(len(listeTweets)) : 
      tweet_time = listeTweets[i].date
      candles = client_bi.get_historical_klines(
        symbol= symbol, 
        interval= Client.KLINE_INTERVAL_1MINUTE, 
        start_str= int(datetime.timestamp(tweet_time)*1000-3601000), 
        end_str= int(datetime.timestamp(tweet_time)*1000+3601000),
        limit= 120 
        )
      x = 0 
      y = 0
      if len(candles)==120:
        for j in range(60) : 
          x = x + float(candles[j][5])
          y = y + float(candles[j+60][5])
        var_v = ((y/x)-1)*100
        var_c_brut = float(candles[119][4]) - float(candles[60][1])
        var_c = (var_c_brut/float(candles[60][1]))*100
      else:
        var_c=np.NaN
        var_v=np.NaN
      df = pd.DataFrame(np.array([listeTweets[i].id, listeTweets[i].date, var_c, var_v], ndmin=2), columns=['Tweet','Date','Variation du cours (en %)', 'Variation du volume (en %)'])
      data=data.append(df)    

  else:
    for i in range(len(listeTweets)) :
      tweet_time = listeTweets[i].date
      candles = client_bi.get_historical_klines(
        symbol = symbol, 
        interval = Client.KLINE_INTERVAL_1HOUR, 
        start_str = int(datetime.timestamp(tweet_time)*1000-86401000), 
        end_str = int(datetime.timestamp(tweet_time)*1000+86401000),
        limit = 48 
        )
      x = 0 
      y = 0
      if len(candles)==48:
        for j in range(24) : 
          x = x + float(candles[j][5])
          y = y + float(candles[j+24][5])
        var_v = ((y/x)-1)*100
        var_c_brut = float(candles[47][4]) - float(candles[24][1])
        var_c = (var_c_brut/float(candles[24][1]))*100
      else:
        var_c=np.NaN
        var_v=np.NaN
      df = pd.DataFrame(np.array([listeTweets[i].id, listeTweets[i].date, var_c, var_v], ndmin=2), columns=['Tweet','Date','Variation du cours (en %)', 'Variation du volume (en %)'])
      data=data.append(df)
        
  moyenne_c = data.iloc[:,2].mean(skipna=True)
  moyenne_v = data.iloc[:,3].mean(skipna=True)
  print ('La moyenne des variations du cours sur '+Interval+'h est de', f'{moyenne_c:.3f}','%, après un tweet de '+Username)
  print ('La moyenne des variations des volumes sur '+Interval+'h est de', f'{moyenne_v:.3f}','%, après un tweet de '+Username)
  return(data)

#===============FONCTION QUI TRACE LE COURS CORRESPONDANT AUX TWEETS LES PLUS IMPACTANTS===============
import numpy as np
import pandas as pd

def Plot_MostImpactfulTweets(listofTweets,ImpactofTweets, params):
  ImpactofTweets = ImpactofTweets.sort_values(by='Variation du cours (en %)', ascending=False)
  ImpactofTweets.index = pd.RangeIndex(ImpactofTweets.shape[0])

  for i in enumerate(listofTweets):
    if i[1].id==ImpactofTweets["Tweet"][0]:
      i[1].draw(params)

  for i in enumerate(listofTweets):
    if i[1].id==ImpactofTweets.dropna().tail(1)["Tweet"].values:
      i[1].draw(params)

#===============FONCTION QUI AFFICHE LA LISTE DES TWEETS===============
def Afficher(listofTweets):
  for i in enumerate(listofTweets):
    print(i[1])

#===============FONCTION QUI TRACE LE COURS CORRESPONDANT A L'ID DU TWEET CHOISI===============

def Plot_Tweet(listofTweets, params, id):
  x=0
  for i in enumerate(listofTweets):
    if i[1].id==id:
      i[1].draw(params)
      x=1
  if x==0:
    print("L'id n'est pas bon")
