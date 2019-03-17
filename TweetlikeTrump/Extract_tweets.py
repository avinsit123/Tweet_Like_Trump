import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy.streaming import StreamListener
import csv

import json


def process_or_store(tweet):
    json.dumps(tweet)



auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def Query_tweets(api,query):
    for tweet in  tweepy.Cursor(api.search,
                           q=query,
                           rpp=1000,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items(10):
        process_or_store(tweet._json)
        return status

def user_tweets(api,screen_name):
    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200,tweet_mode="extended")

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest,tweet_mode="extended")

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print
        "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.full_text.encode('ascii', errors='ignore')] for tweet in alltweets]

    # write the csv
    print(outtweets)

    with open('Tweets of Trump.txt', 'w') as f:
        for item in outtweets:
            f.write("%s\n" % item)




class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.txt', 'a') as f:
                f.write(data)
                print(type(data))
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__=="__main__":
    #twitter_stream = Stream(auth, MyListener())
    #twitter_stream.filter(track=['@realDonaldTrump'])
    user_tweets(api,"@realDonaldTrump")
