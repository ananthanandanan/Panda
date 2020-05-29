import tweepy
from datetime import date
import pandas as  pd

def nawab_get_id():
        ### Read the last retweeted id from a file
        tid_store = pd.read_csv('tid_store.csv')
        return tid_store['Id'] 
    
def main():

    consumer_key = 'M7Or3e6x1pByV0y4ycGVQX25Q'
    consumer_secret = 'r8nvKpmsq96xKaifGHofk2VIleXPR8QSDa7td5Yp9tDDz6Kq75'
    access_token = '786588110624653313-38yuLzjviUt4i5CGcLfiEOvmVo8zJXD'
    access_token_secret =  '8WJGWMl6J8EVHYsyAOQi2IqE8EqogdOqBoHNF2tBt9h6U'

    latest_date = date.today()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tid_list = nawab_get_id()
    for id in tid_list:
        try:
            print(type(id))
            USer = api.get_status(id=id)
            username = USer.author.screen_name
            url = "https://twitter.com/" + username + "/status/" + str(id)
            print(url)
        except tweepy.TweepError as e:
            print("no such url")
            
if __name__ == "__main__":
    
    main()

