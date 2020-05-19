import tweepy
from datetime import date


consumer_key = 'M7Or3e6x1pByV0y4ycGVQX25Q'
consumer_secret = 'r8nvKpmsq96xKaifGHofk2VIleXPR8QSDa7td5Yp9tDDz6Kq75'
access_token = '786588110624653313-38yuLzjviUt4i5CGcLfiEOvmVo8zJXD'
access_token_secret =  '8WJGWMl6J8EVHYsyAOQi2IqE8EqogdOqBoHNF2tBt9h6U'

latest_date = date.today()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
admin = api.me()
username = admin.screen_name
print(type(username))
"""def main():
    
    try:
        for tweets in tweepy.Cursor(api.search, q="#HTTPS", tweet_mode="extended",lang='en', since=latest_date).items(1):
            user = tweets.user.screen_name
            text = tweets.full_text
            print(str(text))
        
    except tweepy.TweepError as e:
        print("some error",e.reason)       


if __name__ == "__main__":
    
    main()"""
