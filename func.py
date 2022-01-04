#===============FONCTION QUI RECUPERE ET TRI LES TWEETS QUI NOUS INTERESSENT===============
import tweepy
from datetime import datetime
from cryptoDict import CryptoDict
from API_KEY import key,secret,access,access_s,bearer
from classes import Params, Tweet

def Get_Relevant_Tweets(Username, Symbol):
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

def Plot_Historical(listeTweets, histKlines):
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
