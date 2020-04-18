import tweepy

consumer_key = '4z*********************oF'
consumer_secret = '6P**********************************************3T'
access_token = '79**********************************************nA'
access_token_secret = 'PS*****************************************dO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

queries = ["rt to win", "retweet to win"]
tweets_per_query  = 50

new_tweets = 0
for querry in queries:
    print ("Starting new querry: " + querry)
    for tweet in tweepy.Cursor(api.search, q=querry, tweet_mode="extended").items(tweets_per_query ):

        user = tweet.user.screen_name
        id = tweet.id
        url = 'https://twitter.com/' + user +  '/status/' + str(id)
        print (url)

        try:
            text = tweet.retweeted_status.full_text.lower()
        except:
            text = tweet.full_text.lower()
        if "retweet" in text or "rt" in text:
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    print("\tRetweeted")
                    new_tweets += 1
                except tweepy.TweepError as e:
                    print('\tAlready Retweeted')

        if "like" in text or "fav" in text:
            try:
                tweet.favorite()
                print('\t' + "Liked")
            except:
                print('\tAlready Liked')
        if "follow" in text:
            try:
                to_follow = [tweet.retweeted_status.user.screen_name] + [i['screen_name'] for i in tweet.entities['user_mentions']]
               # Don't follow origin user (person who retweeted)
            except:
                to_follow = [user] + [i['screen_name'] for i in tweet.entities['user_mentions']]

            for screen_name in list(set(to_follow)):
                api.create_friendship(screen_name)
                print('\t' + "Followed: " + screen_name)

print ("New Tweets: " + str(new_tweets))