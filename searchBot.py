import tweepy
import time

api_key = '7s3meBayAGtanvhzGCN2GM3aL'
api_secret = 'DoRmF9ZX81aYeixIYvZc9ES1v3I5vEY5O5gn4hxUoLcIMHaQBC'

access_token = '1433875643108769794-34Ags3opfJuuzTNpTaj7l9TbeJ6JjC'
access_secret = 'bjxNijw8B33C3ZpJ2OZuxgnIkngfhzkWUyJbMm0KZHMBU'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

hashtag = "insert_select_hashtag_here"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("insert_message_here")
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)

searchBot()