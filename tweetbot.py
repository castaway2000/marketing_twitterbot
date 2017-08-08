import tweepy
import time

from credentials import settings
from twitter_stream import twstream


def reply(api, tweet):
    # get the most recent tweet from the user
    tweet_id = tweet['id']
    # to create a reply you simply @ and mark the tweet id
    api.update_status(".@"+tweet['user']+" have you heard of tourzan.com its a good travel resource. "
                                "the blogs and guides are top notch.", tweet_id)


def time_line(api):
    keywords = ['@twitter', 'tourist', 'traveling', 'tours', 'tour guides', 'tours for the disabled', 'ADA tours',
                'tours for kids', 'jobs for college students', 'jobs for the elderly', 'travel guide', 'international',
                'overseas']
    timeline = twstream.TwitterStream()
    stream = timeline.tweet_stream(api.auth, keywords)
    return timeline.decoder(stream)


def main():
    """auth section of code"""
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

