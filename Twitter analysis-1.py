import tweepy
from tweepy import OAuthHandler

class Twitter():
    #use your twitter keys
    consumer_key='*********************************' #give your consumer_key
    consumer_secret='*********************************'#give your consumer_secret
    access_token='*******************************'#give your access_token
    access_secret='******************************'#give your access_secret
    def __init__(self,feed_count=10):
       self.feed_count = feed_count
    def authenticate(self):
       auth = OAuthHandler(Twitter.consumer_key, Twitter.consumer_secret)
       auth.set_access_token(Twitter.access_token, Twitter.access_secret)
       api = tweepy.API(auth)
       print("Connection to the twitter api established.")
       return api
    def getFeed(self,api):
       for tweet in tweepy.Cursor(api.home_timeline).items(self.feed_count):
           print(tweet.text)
t = Twitter(100)
api_obj = t.authenticate()
t.getFeed(api_obj)