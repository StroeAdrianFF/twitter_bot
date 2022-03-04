from os import truncate
import config
import tweepy
from googletrans import Translator

api_key = config.api_key
api_key_secret = config.api_key_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

# get status from certain user with the help of a user_id. Set tweet mode to show the whole tweet
tweet_list = api.get_status(1499486498055458817, tweet_mode="extended")


trans = Translator()
t = trans.translate(tweet_list.full_text, dest='ro')
print(t.text)
