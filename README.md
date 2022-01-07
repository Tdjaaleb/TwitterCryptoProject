# TwitterCryptoProject

## Classes

### Tweet

#### <u>Attributes</u>

Tweet.id {int} <br>
> Id du tweet <br>

<i>Tweet.author {str}</i> <br>
> Auteur du tweet (nom d'utilisateur) <br>

Tweet.text {str} <br>
> Contenu du tweet <br>

Tweet.date {datetime.datetime} <br>
> Date du tweet <br>

Tweet.type {str} <br>
> Type de tweet <br>

Tweet.candles {pandas.DataFrame} <br>
> Dataframe des données financières avant et après le tweet sur une cryptomonnaie <br>

Tweet.priceInf {float} <br>
> Variation du prix arpès le tweet <br>

Tweet.volumeInf {float} <br>
> Variation du volume avant/après le tweet <br>

#### Methods

Tweet.__init__(self, id, author, text, date, type) <br>
Tweet.__str__(self) <br>
Tweet.get_klines(self, params) <br>
Tweet.get_influence(self, params) <br>
Tweet.draw(self, params) <br>

### ResponseTweet(Tweet)

#### Attributes

ResponseTweet.id {int} <br>
ResponseTweet.author {str} <br>
ResponseTweet.text {str} <br>
ResponseTweet.date {datetime.datetime} <br>
ResponseTweet.answeringTo {str} <br>
ResponseTweet.type {str} <br>
ResponseTweet.candles {pandas.DataFrame} <br>
ResponseTweet.priceInf {float} <br>
ResponseTweet.volumeInf {float} <br>

#### Methods

ResponseTweet.__init__(self, tweet, answeringTo) <br>
ResponseTweet.__str__(self) <br>
ResponseTweet.get_klines(self, params) <br>
ResponseTweet.get_influence(self, params) <br>
ResponseTweet.draw(self, params) <br>

### Retweet(Tweet)

#### Attributes

Retweet.id {int} <br>
Retweet.author {str} <br>
Retweet.text {str} <br>
Retweet.date {datetime.datetime} <br>
Retweet.original_author {str} <br>
Retweet.type {str} <br>
Retweet.candles {pandas.DataFrame} <br>
Retweet.priceInf {float} <br>
Retweet.volumeInf {float} <br>

#### Methods

Retweet.__init__(self, tweet, original_author) <br>
Retweet.__str__(self) <br>
Retweet.get_klines(self, params) <br>
Retweet.get_influence(self, params) <br>
Retweet.draw(self, params) <br>


