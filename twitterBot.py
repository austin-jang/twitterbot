import tweepy
import time

API_KEY = '7s3meBayAGtanvhzGCN2GM3aL'
API_SECRET = 'DoRmF9ZX81aYeixIYvZc9ES1v3I5vEY5O5gn4hxUoLcIMHaQBC'
ACCESS_TOKEN = '1433875643108769794-34Ags3opfJuuzTNpTaj7l9TbeJ6JjC'
ACCESS_SECRET = 'bjxNijw8B33C3ZpJ2OZuxgnIkngfhzkWUyJbMm0KZHMBU'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def retrieve_last_seen_id(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen_id(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    mentions = api.mentions_timeline(retrieve_last_seen_id(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(mentions):
        if '#insert_select_hashtag_here' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + "Insert_reply_here", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen_id(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)