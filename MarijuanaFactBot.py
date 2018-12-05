import Tkinter
import tweepy

marijuana_text = open("MarijuanaFacts.txt", "r")
textRead = marijuana_text.read()
print(textRead)

# Keys
consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This checks API is working by returning username of twitter account
user = api.me()
print (user.name)

# Follows everyone that follows you
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

# Sends out the tweets
for fact in marijuana_text:
    api.update_status(status =str(fact))
    time.sleep(10)