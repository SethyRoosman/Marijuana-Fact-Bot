import tweepy
import time

tweeting = True

marijuana_text = open("MarijuanaFacts.txt", "r")
#textRead = marijuana_text.read()
textFacts = marijuana_text.readlines()
#splitFacts = str(textRead.split(","))
#print(textRead)

# Keys
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXX'
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
#if tweeting == True:

#api.update_status(status =str("The most common marijuana isused is smoking"))
for fact in textFacts:
    api.update_status(status =str(fact))
    print("Tweeting")
    time.sleep(43200)
