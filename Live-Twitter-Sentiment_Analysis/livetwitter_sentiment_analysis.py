# -*- coding: utf-8 -*-
"""LiveTwitter_Sentiment_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DtDnpW7L0pgLYH23ExGeiA62NI5Kry0O
"""

import tweepy
from textblob import TextBlob

consumer_key = ''

consumer_key_secret = ''

access_token = ''

access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Andres Manuel López Obrador')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:
       print ('Positive')
    elif analysis.sentiment[0]<0:
       print ('Negative')
    else:
       print ('Neutral')