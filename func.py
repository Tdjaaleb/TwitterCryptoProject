
from API_KEY import bearer,key,secret,access,access_s
import tweepy
from datetime import datetime
from cryptoDict import CryptoDict
from classes import Tweet, Twittos, ResponseTweet, Retweet
import pandas as pd

#===============FONCTION QUI RECUPERE ET TRI LES TWEETS QUI NOUS INTERESSENT===============
def Get_Relevant_Tweets(params):
    Username=params["user"]
    Symbol=params["symbol"]
    client_twi = tweepy.Client(
        bearer_token = bearer,
        consumer_key = key,
        consumer_secret = secret,
        access_token = access,
        access_token_secret = access_s
    )

    user = client_twi.get_user(username = Username, user_fields = 'public_metrics') #Récupère les informations de l'utilisateur en fonction de son nom d'utilisateur

    if user.data==None:
        print("L'utilisateur n'existe pas")
        return(None)

    user_id = user.data["id"] #Id utilisateur
    iter_max = int(user.data.public_metrics["tweet_count"]/100)+1 #Nb de tweets divisé par 100 pour créer la boucle

    timer = str(datetime.utcnow())
    timer = timer.replace(' ','T')
    timer = timer.split('.')[0]+'Z'

    Author = Twittos(user_id=user_id, username=params['user'], Crypto=params['symbol'])

    for i in range(iter_max):
        Tweets = client_twi.get_users_tweets(id=user_id, max_results=100, tweet_fields='created_at', end_time=timer)
        if type(Tweets.data)==list:
            for j in enumerate(Tweets.data):
                for k in enumerate(CryptoDict[Symbol]):
                    if j[1].text.lower().find(k[1])!=-1:
                        x = Tweet(id = Tweets.data[j[0]]["id"], author = Username, text = Tweets.data[j[0]]["text"], date = Tweets.data[j[0]].created_at)
                        if j[1].text.find('@')==0:
                            answering = j[1].text.split('@')[1]
                            answering = answering.split(' ')[0]
                            x = ResponseTweet(x, answeringTo = answering)
                        elif j[1].text.lower().find('rt')==0:
                            originalAuth=j[1].text.split('@')[1]
                            originalAuth=originalAuth.split(':')[0]
                            x = Retweet(original_author=originalAuth)
                        Author.add(x)
                timer = str(Tweets.data[j[0]].created_at)
                timer = timer.replace(' ','T')
                timer = timer.split('+')[0]+'Z'
    return(Author)

#===============FONCTION QUI TRACE LE COURS CORRESPONDANT AUX TWEETS LES PLUS IMPACTANTS===============
def Plot_MostImpactfulTweets(Author, params):
    tweetsid=[]
    tweetsimpact=[]
    for i in enumerate(Author.Tweets):
        tweetsid.append(i[1].id)
        tweetsimpact.append(i[1].priceInf)
    df = {
        "id" : tweetsid,
        "impact" : tweetsimpact
    }
    ImpactofTweets = pd.DataFrame(df)
    ImpactofTweets = ImpactofTweets.sort_values(by='impact', ascending=False)
    ImpactofTweets.index = pd.RangeIndex(ImpactofTweets.shape[0])

    for i in enumerate(Author.Tweets):
        if i[1].id==ImpactofTweets["id"][0]:
            i[1].draw(params)

    for i in enumerate(Author.Tweets):
        if i[1].id==ImpactofTweets.dropna().tail(1)["id"].values:
            i[1].draw(params)
