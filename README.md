# TwitterCryptoProject

## Classes

### Tweet

#### Attributes

Tweet.id {int} n/
Tweet.author {str}
Tweet.text {str}
Tweet.date {datetime.datetime}
Tweet.type {str}
Tweet.candles {pandas.DataFrame}
Tweet.priceInf {float}
Tweet.volumeInf {float}

#### Methods

Tweet.__init__(self, id, author, text, date, type)
Tweet.__str__(self)
Tweet.get_klines(self, params)
Tweet.get_influence(self, params)
Tweet.draw(self, params)

### ResponseTweet(Tweet)

#### Attributes

ResponseTweet.id {int}
ResponseTweet.author {str}
ResponseTweet.text {str}
ResponseTweet.date {datetime.datetime}
ResponseTweet.answeringTo {str}
ResponseTweet.type {str}
ResponseTweet.candles {pandas.DataFrame}
ResponseTweet.priceInf {float}
ResponseTweet.volumeInf {float}

#### Methods

ResponseTweet.__init__(self, tweet, answeringTo)
ResponseTweet.__str__(self)
ResponseTweet.get_klines(self, params)
ResponseTweet.get_influence(self, params)
ResponseTweet.draw(self, params)

### Retweet(Tweet)

#### Attributes

Retweet.id {int}
Retweet.author {str}
Retweet.text {str}
Retweet.date {datetime.datetime}
Retweet.original_author {str}
Retweet.type {str}
Retweet.candles {pandas.DataFrame}
Retweet.priceInf {float}
Retweet.volumeInf {float}

#### Methods

Retweet.__init__(self, tweet, original_author)
Retweet.__str__(self)
Retweet.get_klines(self, params)
Retweet.get_influence(self, params)
Retweet.draw(self, params)


