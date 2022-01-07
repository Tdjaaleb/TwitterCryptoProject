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

    #Initialisation du client Tweepy pour l'API Twitter
    client_twi = tweepy.Client(
        bearer_token = bearer,
        consumer_key = key,
        consumer_secret = secret,
        access_token = access,
        access_token_secret = access_s
    )
    #Requete qui permet la récupération des informations de l'utilisateur twitter en fonction de son nom d'utilisateur
    user = client_twi.get_user(username = Username, user_fields = 'public_metrics')

    #Cas où le nom d'utilisateur n'existe pas
    if user.data==None:
        print("L'utilisateur n'existe pas")
        return(None)

    #Id utilisateur
    user_id = user.data["id"]
    #Nb de tweets divisé par 100 pour créer la boucle
    iter_max = int(user.data.public_metrics["tweet_count"]/100)+1

    #Initialisation de la date à celle d'aujourd'hui / le format de date que l'API Twitter utilise est un format un peu spécial mais qui est de type datetime.datetime
    timer = str(datetime.utcnow())
    timer = timer.replace(' ','T')
    timer = timer.split('.')[0]+'Z'

    #Création d'une variable "Author" de classe "Twittos"
    Author = Twittos(user_id=user_id, username=params['user'], Crypto=params['symbol'])

    #Boucle qui permet la récupération de tous les tweets (limité au 3200 plus récents) et qui rempli la variable Author
    for i in range(iter_max):
        #Requete qui permet de récupérer les 100 tweets les plus récents à partir de la date "timer"
        Tweets = client_twi.get_users_tweets(id=user_id, max_results=100, tweet_fields='created_at', end_time=timer)
        #Si la requete est réussi, l'objet Tweets.data est de type "list"
        if type(Tweets.data)==list:
            #Parmi tous les tweets récupérés
            for j in enumerate(Tweets.data):
                #Parmi tous les mots en relation avec la cryptomonnaie (cf cryptoDict.py)
                for k in enumerate(CryptoDict[Symbol]):
                    #Si le mot est détecté dans le tweet
                    if j[1].text.lower().find(k[1])!=-1:
                        #On crée un objet de class "Tweet" et on lui assigne les différents attributs nécessaire
                        x = Tweet(id = Tweets.data[j[0]]["id"], author = Username, text = Tweets.data[j[0]]["text"], date = Tweets.data[j[0]].created_at)
                        #Si le tweet commence par le caractère "@", c'est une réponse à un tweet, on transforme donc l'objet en objet de classe ResponseTweet
                        if j[1].text.find('@')==0:
                            answering = j[1].text.split('@')[1]
                            answering = answering.split(' ')[0]
                            x = ResponseTweet(x, answeringTo = answering)
                        #Si le tweet commence par les caractères "rt", c'est un retweet, on transforme donc l'objet en objet de classe Retweet
                        elif j[1].text.lower().find('rt')==0:
                            originalAuth=j[1].text.split('@')[1]
                            originalAuth=originalAuth.split(':')[0]
                            x = Retweet(original_author=originalAuth)
                        #On ajoute l'objet à l'objet de classe Author (il est précisement ajouté à Author.Tweets qui est une liste)
                        Author.add(x)
                #La date devient la date du tweet le plus ancien de la requête
                timer = str(Tweets.data[j[0]].created_at)
                timer = timer.replace(' ','T')
                timer = timer.split('+')[0]+'Z'
    #L'objet retourné est l'objet Author de classe "Twittos"
    return(Author)

#===============FONCTION QUI TRACE LE COURS CORRESPONDANT AUX TWEETS LES PLUS IMPACTANTS===============
def Plot_MostImpactfulTweets(Author, params):
    #Création d'une dateframe qui contient les ids de tweets de l'auteur ainsi que leur impact sur le cours
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
    #Tri de la dataframe du tweet le plus bénéfique au tweet le plus néfaste (pour le prix de la cryptomonnaie)
    ImpactofTweets = ImpactofTweets.sort_values(by='impact', ascending=False)
    #Réindexage de la dataframe
    ImpactofTweets.index = pd.RangeIndex(ImpactofTweets.shape[0])

    #Permet de rechercher le tweet qui à eu le plus d'impact à la hausse et trace le graphique correspondant
    for i in enumerate(Author.Tweets):
        if i[1].id==ImpactofTweets["id"][0]:
            i[1].draw(params)

    #Permet de rechercher le tweet qui à eu le plus d'impact à la baisse et trace le graphique correspondant
    for i in enumerate(Author.Tweets):
        if i[1].id==ImpactofTweets.dropna().tail(1)["id"].values:
            i[1].draw(params)
