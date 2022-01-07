# TwitterCryptoProject

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

### ResponseTweet(Tweet)

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

### Retweet(Tweet)

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

## Functions

### Get_Relevant_Tweets(params)
<i>input : dict({"user","symbol","currency","interval"})</i> <br>
<i>response : Class(Author)</i> <br>
> Permet de récupérer les tweets de l'utilisateur choisi sur une cryptomonnaie choisie <br>


### Plot_MostImpactfulTweets(Author, params)
<i>input : Class(Author), dict({"user","symbol","currency","interval"})</i> <br>
<i>response : None</i>
> Permet de tracer les courbes de prix d'une cryptomonnaie avant/après pour le tweet le plus influent à la hausse et le plus influent à la baisse <br>

