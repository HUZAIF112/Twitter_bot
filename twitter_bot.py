import random
import tweepy


#set up connection to twitter via 'tweepy'
CONSUMER_KEY = "wWHsX1VD84IgHolscmx1HD6Y7"
CONSUMER_SECRET = "I9bqgGDOiIVExOOh7LMMnLTjaa77cScKbHQDjGJvXuWeFfWv"
ACCESS_KEY = "1583433420864192512-tk8TjBt2KUSQPHuNiPUztw9hJCUHTy"
ACCESS_SECRET = "5s5epVjmqAkl2pd1yQfNzpuXmlVCeHkeXNFKb5u0SZLja"
BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAJewiQEAAAAAm05dacr%2FXGezLgMx5CI9hfcwPcA%3DtAuezno874oMPm5TV1aERWbSDo3fiW5LCIWwqQryIliClUt5zZ"

client = tweepy.Client(BEARER_TOKEN,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
api= tweepy.API(auth)


# A list containing replies that are then randomly chosen using a variable
replies= ['sounds interesting tell me more','I would love to know more. Could i DM you?','how would i go about implementing this?','Thanks for sharing!']
generate_replies= random.choice(replies)



#create stream class to like,retweet and reply
class mystream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        try:
            client.retweet(tweet.id)
            client.like(tweet.id)
            client.create_tweet(in_reply_to_tweet_id=tweet.id,text=generate_replies)

        except Exception as error:
            print(error)    


stream = mystream(bearer_token=BEARER_TOKEN)

# look for tweets with these specific rules
rule = tweepy.StreamRule("(#learnprogramming OR #learnpython)(-is:reply -is:retweet )")

stream.add_rules(rule)

stream.filter()





