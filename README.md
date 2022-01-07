# TwitterCryptoProject

## Sommaire
1. [Notice](#Notice)
2. [Functions](#Functions)
  * [Get_Relevant_Tweets](#Get_Relevant_Tweets)
  * [Plot_MostImpactfulTweets](#Plot_MostImpactfulTweets)
3. [Classes](#Classes)
  * [Tweet](#Tweet)
  * [ResponseTweet](#Tweet)
  * [Retweet](#Retweet)
  * [Twittos](#Twittos)

## Notice

1. Remplissez les informations de votre API Twitter dans le fichier 'API_KEY.py'
2. Installez les librairies requises aux versions correspondantes à l'utilisation de l'application (cf 'requirements.txt')
3. Executez le fichier 'main.py'
4. Remplissez les champs demandés par l'application (Username, Symbol (cryptomonnaie), Currency, Interval (intervalle d'analyse))
5. Attendez jusqu'à voir apparaître les graphiques d'analyse
6. Executez les fonctions supplémentaires mises à disposition ou bien fermez l'application

## Functions

### Get_Relevant_Tweets
<i>input : dict({"user","symbol","currency","interval"})</i> <br>
<i>response : Class(Author)</i> <br>
> Permet de récupérer les tweets de l'utilisateur choisi sur une cryptomonnaie choisie <br>

### Plot_MostImpactfulTweets
<i>input : Class(Author), dict({"user","symbol","currency","interval"})</i> <br>
<i>response : None</i>
> Permet de tracer les courbes de prix d'une cryptomonnaie avant/après pour le tweet le plus influent à la hausse et le plus influent à la baisse <br>

## Classes

### Tweet

#### Attributes

<i>Tweet.id {int}</i> <br>
> Id du tweet <br>

<i>Tweet.author {str}</i> <br>
> Auteur du tweet (nom d'utilisateur) <br>

<i>Tweet.text {str}</i> <br>
> Contenu du tweet <br>

<i>Tweet.date {datetime.datetime}</i> <br>
> Date du tweet <br>

<i>Tweet.type {str}</i> <br>
> Type de tweet <br>

<i>Tweet.candles {pandas.DataFrame}</i> <br>
> Dataframe des données financières avant et après le tweet sur une cryptomonnaie <br>

<i>Tweet.priceInf {float}</i> <br>
> Variation du prix arpès le tweet <br>

<i>Tweet.volumeInf {float}</i> <br>
> Variation du volume avant/après le tweet <br>

#### Methods

<i>Tweet.__init__(self, id, author, text, date, type)</i> <br>
> Initialisation <br>

<i>Tweet.__str__(self)</i> <br>
> Affichage <br>

<i>Tweet.get_klines(self, params)</i> <br>
> Permet la récupération des données financières <br>

<i>Tweet.get_influence(self, params)</i> <br>
> Permet le calcul de l'influence d'un tweet sur le volume et le prix d'une cryptomonnaie <br>

<i>Tweet.draw(self, params)</i> <br>
> Permet de tracer la courbe avant/après un tweet du prix d'une cryptomonnaie <br>

### ResponseTweet

#### Attributes

<i>ResponseTweet.id {int}</i> <br>
> Id du tweet <br>

<i>ResponseTweet.author {str}</i> <br>
> Auteur du de la réponse (nom d'utilisateur) <br>

<i>ResponseTweet.text {str}</i> <br>
> Contenu du tweet <br>

<i>ResponseTweet.date {datetime.datetime}</i> <br>
> Date du tweet <br>

<i>ResponseTweet.answeringTo {str}</i> <br>
> Utilisateur à qui répond le tweet <br>

<i>ResponseTweet.type {str}</i> <br>
> Type de tweet <br>

<i>ResponseTweet.candles {pandas.DataFrame}</i> <br>
> Dataframe des données financières avant et après le tweet sur une cryptomonnaie <br>

<i>ResponseTweet.priceInf {float}</i> <br>
> Variation du prix arpès le tweet <br>

<i>ResponseTweet.volumeInf {float}</i> <br>
> Variation du volume avant/après le tweet <br>

#### Methods

<i>ResponseTweet.__init__(self, tweet, answeringTo)</i> <br>
> Initialisation <br>

<i>ResponseTweet.__str__(self)</i> <br>
> Affichage <br>

<i>ResponseTweet.get_klines(self, params)</i> <br>
> Permet la récupération des données financières <br>

<i>ResponseTweet.get_influence(self, params)</i> <br>
> Permet le calcul de l'influence d'un tweet sur le volume et le prix d'une cryptomonnaie <br>

<i>ResponseTweet.draw(self, params)</i> <br>
> Permet de tracer la courbe avant/après un tweet du prix d'une cryptomonnaie <br>

### Retweet

#### Attributes

<i>Retweet.id {int}</i> <br>
> Id du tweet <br>

<i>Retweet.author {str}</i> <br>
> Auteur du retweet (nom d'utilisateur) <br>

<i>Retweet.text {str}</i> <br>
> Contenu du tweet <br>

<i>Retweet.date {datetime.datetime}</i> <br>
> Date du tweet <br>

<i>Retweet.original_author {str}</i> <br>
> Utilisateur qui a posté le tweet <br>

<i>Retweet.type {str}</i> <br>
> Type de tweet <br>

<i>Retweet.candles {pandas.DataFrame}</i> <br>
> Dataframe des données financières avant et après le tweet sur une cryptomonnaie <br>

<i>Retweet.priceInf {float}</i> <br>
> Variation du prix arpès le tweet <br>

<i>Retweet.volumeInf {float}</i> <br>
> Variation du volume avant/après le tweet <br>

#### Methods

<i>Retweet.__init__(self, tweet, original_author)</i> <br>
> Initialisation <br>

<i>Retweet.__str__(self)</i> <br>
> Affichage <br>

<i>Retweet.get_klines(self, params)</i> <br>
> Permet la récupération des données financières <br>

<i>Retweet.get_influence(self, params)</i> <br>
> Permet le calcul de l'influence d'un tweet sur le volume et le prix d'une cryptomonnaie <br>

<i>Retweet.draw(self, params)</i> <br>
> Permet de tracer la courbe avant/après un tweet du prix d'une cryptomonnaie <br>

### Twittos

#### Attributes

<i>Twittos.user_id {int}</i> <br>
> Id de l'utilisateur <br>

<i>Twittos.username {str}</i> <br>
> Nom de l'utilisateur <br>

<i>Twittos.Crypto {str}</i> <br>
> Cryptomonnaie sur laquelle l'analyse est faite <br>

<i>Twittos.NbTweet {int}</i> <br>
> Nombre de Tweets parlant de la cryptomonnaie <br>

<i>Twittos.Tweets {list}</i> <br>
> Liste de tous les tweets parlant de la cryptomonnaie (les éléments de la liste sont de types Tweet, Retweet ou ResponseTweet <br>

<i>Twittos.priceInf {float}</i> <br>
> Influence moyenne d'un tweet sur le prix de la cryptomonnaie <br>

<i>Twittos.volumeInf {float}</i> <br>
> Influence moyenne d'un tweet sur le volume d'échange de la cryptomonnaie <br>

#### Methods

<i>Twittos.__init__(self, user_id,username, Crypto)</i> <br>
> Initialisation <br>

<i>Twittos.__str__(self)</i> <br>
> Affichage <br>

<i>Twittos.Afficher_Tweets(self, type)</i> <br>
> Affiche tous les tweets de l'utilisateur, type permet de choisir quels tweets affichés (all, tweet, retweet, response) <br>

<i>Twittos.add(self, Tweet)</i> <br>
> Ajoute un tweet à la liste Twittos.Tweets <br>

<i>Twittos.remove_duplicates(self)</i> <br>
> Supprime les tweets en doublon dans la liste Twittos.Tweets <br>

<i>Twittos.get_influence(self, params)</i> <br>
> Calcule l'influence moyenne d'un tweet de l'utilisateur sur le prix et le volume d'une cryptomonnaie <br>

<i>Twittos.draw(self, params)</i> <br>
> Trace le graphique historique du prix de la cryptomonnaie avec tous les tweets affichés aux dates correspondantes <br>

<i>Twittos.Plot_Tweet(self, params, id)</i> <br>
> Trace le graphique avant/après un tweet du prix de la cryptomonnaie selon l'id du tweet sélectionnés <br>
