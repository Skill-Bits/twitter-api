import tweepy
import sys

class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        print(status.text)
    def on_error(self,status_code):
        print(status_code)


consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=["news"])
