#Import des fonctions
from func import Get_Relevant_Tweets, Plot_MostImpactfulTweets

#Demande à l'utilisateur de rentrer un "@" twitter
Username = input("Veuillez entrer l'identifiant Twitter de l'utilisateur : ")

#Demande à l'utilisateur de choisir un cryptomonnaie
Symbol = input("Quelle cryptomonnaie souhaitez vous analyser ? (BTC/ETH/AVAX/DOGE/BNB) ")
while Symbol!="BTC" and Symbol!="ETH" and Symbol!="AVAX" and Symbol!="DOGE" and Symbol!="BNB":
    Symbol = input("Veuillez entrer une cryptomonnaie disponible pour analyse (BTC, ETH, AVAX, DOGE, BNB) :")

#Demande à l'utilisateur de choisir une monnaie
if Symbol=="AVAX":
    Currency = input("En quelle monnaie voulez-vous analyser les cours ? (EUR/USDT) GBP non disponible pour l'AVAX")
    while Currency!="USDT" and Currency!="EUR":
        Currency = input("Veuillez entrer une monnaie valide (EUR, USDT) GBP non disponible pour l'AVAX : ")
Currency = input("En quelle monnaie voulez-vous analyser les cours ? (EUR/USDT/GBP) ")
while Currency!="USDT" and Currency!="EUR" and Currency!="GBP":
    Currency = input("Veuillez entrer une monnaie valide (EUR, USDT, GBP) : ")

#Demande à l'utilisateur de choisir un interval de temps pour l'analyse
Interval = input("Sur combien de temps souhaitez vous analyser ? ")
while Interval!='1' and Interval!='24':
    Interval = input("Veuillez entrer une intervalle de temps valide pour l'analyse (1 : pour 1heure / 24 : pour 24heure) : ")

#Créer un dictionnaire avec les paramètres renseignés par l'utilisateur
params = {
    "user" : Username,
    "symbol" : Symbol,
    "currency" : Currency,
    "interval" : Interval
}

#Fonction qui permet de récupérer les tweets pertinents selon les paramètres
Author = Get_Relevant_Tweets(params)

#Si le "@" twitter n'existe pas
if Author==None:
    print("Fin de l'analyse")
#Si le "twittos" n'a pas tweeté à propos de la cryptomonnaie
elif Author.Tweets==[]:
    print(Author)
    print("L'utilisateur n'a pas tweeté à propos de "+Symbol)
    print("Fin de l'analyse")
else:
    #Suppression des doublons
    Author.remove_duplicates()
    print(Author)

    #Trace la courbe historique de la cryptomonnaie (chaque bougie représente 1jour) ainsi que les dates des tweets du "twittos" à propos de la cryptomonnaie
    Author.draw(params)

    #Boucle qui permet de récupérer les données financières de la cryptomonnaie pour chaque tweet sur l'interval de temps choisi au début
    #Dans un second temps, la boucle calcul l'influence de chaque tweet sur le cours de la cryptomonnaie et son volume de transaction
    for i, tweet in enumerate(Author.Tweets):
        tweet.get_klines(params)
        tweet.get_influence(params)

    #Calcule l'influence moyenne du "twittos" sur le marché de la cryptomonnaie choisie
    Author.get_influence(params)

    #Trace la courbe historique avant/après du tweet qui a eu le plus d'influence à la hausse
    #Trace également la courbe historique avant/après du tweet qui a eu le plus d'influence à la baisse
    Plot_MostImpactfulTweets(Author, params)

    print("")
    print("Fin de l'analyse")
    print("")
    print("Pour consulter la liste des Tweets, entrez la commande 'Author.Afficher_Tweets(type='')'")
    print("#type='all' --> tous les élemens #type='tweet' --> seulement le tweets #type='retweet' --> seulement les retweets #type='reponse' --> seulement les réponses")
    print("")
    print("Pour tracer l'évolution du cours par rapport à un tweet, entrez la commande 'Author.Plot_Tweet(params, id=)' avec id = l'id du tweet")
