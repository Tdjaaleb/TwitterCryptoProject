from func import Get_Relevant_Tweets, Plot_Historical, MarketAnalysis, Plot_MostImpactfulTweets, Afficher, Plot_Tweet

Username = input("Veuillez entrer l'identifiant Twitter de l'utilisateur : ")

Symbol = input("Quelle cryptomonnaie souhaitez vous analyser ? ") #BTC / ETH / AVAX / BNB / DOGE / ...
while Symbol!="BTC" and Symbol!="ETH" and Symbol!="AVAX" and Symbol!="DOGE" and Symbol!="BNB":
    Symbol = input("Veuillez entrer une cryptomonnaie disponible pour analyse (BTC, ETH, AVAX, DOGE, BNB) :")

Currency = input("En quelle monnaie voulez-vous analyser les cours ? ") #USDT / EUR / GBP
while Currency!="USDT" and Currency!="EUR" and Currency!="GBP":
    Currency = input("Veuillez entrer une monnaie valide (EUR, USDT, GBP) : ")

Interval = input("Sur combien de temps souhaitez vous analyser ? ") #1 Heure / 24 Heures
while Interval!='1' and Interval!='24':
    Interval = input("Veuillez entrer une intervalle de temps valide pour l'analyse (1 : pour 1heure / 24 : pour 24heure) : ")

params = {
    "user" : Username,
    "symbol" : Symbol,
    "currency" : Currency,
    "interval" : Interval
}

Liste_Tweets = Get_Relevant_Tweets(params)

if Liste_Tweets==[]:
    print("L'utilisateur n'a pas tweeté à propos de "+Symbol)
    print("Fin de l'analyse")
elif Liste_Tweets==None:
    print("Fin de l'analyse")
else:
    #Suppression des Tweets en doublon
    ids=[]
    for i,tweets in enumerate(Liste_Tweets):
        ids.append(tweets.id)

    stop = len(ids)-2
    for i in range(len(ids)-1):
        if ids[i]==ids[i+1]:
            Liste_Tweets.remove(Liste_Tweets[i])
            ids.remove(ids[i])
            stop=stop-1
        if i==stop:
            break
        
    Plot_Historical(Liste_Tweets, params)
    
    TweetsImpact = MarketAnalysis(Liste_Tweets, params)

    Plot_MostImpactfulTweets(Liste_Tweets, TweetsImpact, params)

    print("Fin de l'analyse")
    print("Pour consulter la liste des Tweets, entrez la commande 'Afficher(Liste_Tweets)'")
    print("Pour tracer l'évolution du cours par rapport à un tweet, entrez la commande 'Plot_Tweet(Liste_Tweet, params, id)' avec id = l'id du tweet")
