# marketing_twitterbot

as the title says this is a full auto reply bot for twitter using the tweepy API for the read/reply system.
it is designed to target certain keywords or usernames to market a product


## tweetbot.py
 - this is the main file that communicates with the custom libraries in the back that will handle all the workload


## /credentials
  #### settings.py
- add your own keys here


## /twitter_stream
  #### twstream.py
  - this is where the magic really happens. the stream and listeners are located here.
  - returns: username, tweeted message, and tweet id 

