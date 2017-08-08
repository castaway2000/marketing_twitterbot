# Author: Adam Szablya
# Origin Date: 8/8/2017
# marketing twitter bot


import tweepy
import json


class TwitterStreamListener(tweepy.StreamListener):
    """ Tweepy stream listener class"""

    def on_status(self, status):
        """
        :param status: twitter reply
        :return: False if 420 error hits to prevent blacklisting
        """
        print status.text
        if status == 420:
         # returning False in on_data disconnects the stream
            return False


class TwitterStream(object):
    """Twitter stream class"""

    def decoder(self, stream):
        """
        :param stream: json data
        :return: [[username, msg, id]] decoded json into a list of lists
        """
        data = []
        decoded = json.loads(stream)
        # print decoded
        data.append([decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'), decoded['id']])
        return data

    def tweet_stream(self, auth, keywords):
        """
        :param auth: api.auth object
        :param keywords: list of keyword strings
        :return: undecoded json
        """
        stream_listener = TwitterStreamListener()
        stream = tweepy.Stream(auth, stream_listener)
        return stream.listener(track=keywords, async=True)