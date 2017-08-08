# Author: Adam Szablya
# Origin Date: 8/8/2017
# marketing twitter bot

import tweepy
import time

from credentials import settings
from twitter_stream import twstream


def reply(api, tweet):
    """
    replies to all captured tweets
    :param api: tweepy api method
    :param tweet: [[username, msg, id]]
    :return: None
    """
    for t in tweet:
    # to create a reply you simply @ and mark the tweet id
        api.update_status(".@"+t[0]+" have you heard of tourzan.com its a good travel resource. "
                          "the travel tips and guides are top notch.")


def time_line(api):
    """
    reads the timeline for the keywords in question
    :param api: tweepy method
    :return: json format dictionary type data
    """
    keywords = ['@twitter', 'tourist', 'traveling', 'tours', 'tour guides', 'tours for the disabled', 'ADA tours',
                'tours for kids', 'jobs for college students', 'jobs for the elderly', 'travel guide', 'international',
                'overseas']
    timeline = twstream.TwitterStream()
    stream = timeline.tweet_stream(api.auth, keywords)
    return timeline.decoder(stream)


def main():
    """auth section of code"""
    # TODO: store previous id's to prevent spamming
    # TODO: intelligent text
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_KEY, settings.ACCESS_SECRET)
    api = tweepy.API(auth)
    while True:
        for t in time_line(api):
            reply(api, t)
        print 'sleeping'
        time.sleep(5)

if __name__ == '__main__':
    main()

