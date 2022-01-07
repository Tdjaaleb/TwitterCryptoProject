from func import Get_Relevant_Tweets, Plot_MostImpactfulTweets

Username = input("Veuillez entrer l'identifiant Twitter de l'utilisateur : ")

Symbol = input("Quelle cryptomonnaie souhaitez vous analyser ? (BTC/ETH/AVAX/DOGE/BNB)")
while Symbol!="BTC" and Symbol!="ETH" and Symbol!="AVAX" and Symbol!="DOGE" and Symbol!="BNB":
    Symbol = input("Veuillez entrer une cryptomonnaie disponible pour analyse (BTC, ETH, AVAX, DOGE, BNB) :")

Currency = input("En quelle monnaie voulez-vous analyser les cours ? (EUR/USDT/GBP")
while Currency!="USDT" and Currency!="EUR" and Currency!="GBP":
    Currency = input("Veuillez entrer une monnaie valide (EUR, USDT, GBP) : ")

Interval = input("Sur combien de temps souhaitez vous analyser ? ")
while Interval!='1' and Interval!='24':
    Interval = input("Veuillez entrer une intervalle de temps valide pour l'analyse (1 : pour 1heure / 24 : pour 24heure) : ")

params = {
    "user" : Username,
    "symbol" : Symbol,
    "currency" : Currency,
    "interval" : Interval
}

Author = Get_Relevant_Tweets(params)

if Author==None:
    print("Fin de l'analyse")
elif Author.Tweets==[]:
    print(Author)
    print("L'utilisateur n'a pas tweeté à propos de "+Symbol)
    print("Fin de l'analyse")
#Suppression des doublons
else:
    Author.remove_duplicates()
    print(Author)

    Author.draw(params)

    for i, tweet in enumerate(Author.Tweets):
        tweet.get_klines(params)
        tweet.get_influence(params)

    Author.get_influence(params)

    Plot_MostImpactfulTweets(Author, params)

    print("")
    print("Fin de l'analyse")
    print("")
    print("Pour consulter la liste des Tweets, entrez la commande 'Author.Afficher_Tweets(type='')'")
    print("#type='all' --> tous les élemens #type='tweet' --> seulement le tweets #type='retweet' --> seulement les retweets #type='reponse' --> seulement les réponses")
    print("")
    print("Pour tracer l'évolution du cours par rapport à un tweet, entrez la commande 'Author.Plot_Tweet(params, id=)' avec id = l'id du tweet")
