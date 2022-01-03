import tweepy
from datetime import datetime
from cryptoDict import CryptoDict

def Get_Relevant_Tweets(Username):
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
                id = Tweets.data[j[0]]["id"]
                author = Username
                text = Tweets.data[j[0]]["text"]
                date = Tweets.data[j[0]].created_at
                typeoftweet = tweet_type
                answeringTo = answering
              )
            elif j[1].text.lower().find('rt')==0:
              tweet_type = 'retweet'
              x = Tweet(
                id = Tweets.data[j[0]]["id"]
                author = Username
                text = Tweets.data[j[0]]["text"]
                date = Tweets.data[j[0]].created_at
                typeoftweet = tweet_type
              )
            else:
              x = Tweet(
                id = Tweets.data[j[0]]["id"]
                author = Username
                text = Tweets.data[j[0]]["text"]
                date = Tweets.data[j[0]].created_at
              )
            liste.append(Tweets.data[j[0]])
        timer = str(Tweets.data[j[0]].created_at)
        timer = timer.replace(' ','T')
        timer = timer.split('+')[0]+'Z'
  return(liste)
