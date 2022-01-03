import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

import tweepy
from binance.client import Client
from mplfinance.original_flavor import candlestick_ohlc

from API_KEY import key,secret,access,access_s,bearer
from func import Get_Relevant_Tweets
from cryptoDict import CryptoDict

client_bi = Client()

client_twi = tweepy.Client(
    bearer_token = bearer,
    consumer_key = key,
    consumer_secret = secret,
    access_token = access,
    access_token_secret = access_s
)

Username = input("Veuillez entrer l'identifiant Twitter de l'utilisateur : ")
Symbol = input("Quelle cryptomonnaie souhaité vous analyser ? ") #BTC / ETH / AVAX / BNB / DOGE / ...
Currency = input("En quelle monnaie voulez-vous analyser les cours ? ") #USDT / EUR / GBP
Interval = input("sur combien de temps souhaités vous analyser ? ") #1 Heure / 24 Heures

Liste_Tweets = Get_Relevant_Tweets(Username)
