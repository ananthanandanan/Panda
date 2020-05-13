import tweepy


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret =  ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
admin = api.me()
username = admin.screen_name
print(username)


