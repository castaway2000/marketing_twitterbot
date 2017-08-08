import tweepy
import json


class TwitterStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text
        if status == 420:
         # returning False in on_data disconnects the stream
            return False


class TwitterStream(object):

    def decoder(self, stream):
        data = []
        decoded = json.loads(stream)
        data.append([decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')])
        return data

    def tweet_stream(self, auth, keywords):
        stream_listener = TwitterStreamListener()
        stream = tweepy.Stream(auth, stream_listener)
        return stream.listener(track=keywords, async=True)