import tweepy
from datetime import date


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret =  ''

latest_date = date.today()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
tweet = api.get_status(1263297052424863745)
print(tweet.text)

"""admin = api.me()
username = admin.screen_name
print(type(username))
def main():
    
    try:
        for tweets in tweepy.Cursor(api.search, q="#HTTPS", tweet_mode="extended",lang='en', since=latest_date).items(1):
            user = tweets.user.screen_name
            text = tweets.full_text
            print(str(text))
        
    except tweepy.TweepError as e:
        print("some error",e.reason)       


if __name__ == "__main__":
    
    main()"""
