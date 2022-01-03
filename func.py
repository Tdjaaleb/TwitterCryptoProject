import tweepy
from datetime import datetime
from cryptoDict import CryptoDict

def Get_All_Tweets(Username):
  list=[]
  user = client_twi.get_user(
    username = Username,
    user_field = 'public_metrics'
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
        tweet_fields='created_at'
        end_time=timer
    )
    for j in enumerate(Tweets.data):
      for k in enumerate(CryptoDict[Symbol]):
        if j[1].text.lower().find(k[1])!=-1:
          list.append(Tweets.data[j])
          
    timer = Tweets.data[99].created_at
    timer = timer.replace(' ','T')
    timer = timer.split('+')[0]+'Z'
  
  return(list)
  
  
