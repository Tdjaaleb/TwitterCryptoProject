from binance.client import Client
from func import Get_Relevant_Tweets, Plot_Historical

client_bi = Client()

Username = input("Veuillez entrer l'identifiant Twitter de l'utilisateur : ")
Symbol = input("Quelle cryptomonnaie souhaitez vous analyser ? ") #BTC / ETH / AVAX / BNB / DOGE / ...
Currency = input("En quelle monnaie voulez-vous analyser les cours ? ") #USDT / EUR / GBP
Interval = input("Sur combien de temps souhaitez vous analyser ? ") #1 Heure / 24 Heures

params = {
    "user" : Username,
    "symbol" : Symbol,
    "currency" : Currency,
    "interval" : Interval
}

Liste_Tweets = Get_Relevant_Tweets(params)

AllTime_Klines = client_bi.get_klines(
    symbol = Symbol+Currency,
    interval = Client.KLINE_INTERVAL_1DAY,
    limit = 1000
)

Plot_Historical(Liste_Tweets, AllTime_Klines, params)
