import os
import tweepy as tw
from IPython.display import display
import pandas as pd

consumer_key = 'NWR63wSrZQzwl2P97K1l49gKA'
consumer_secret = 'ArQmPgr0FTfa9maTAovxSKGavBWlxmW7ViGfginq3rCte4TEvA'

access_token = '1374368783955980290-Rbz7Y7U9nuniN1FiZXiq9lb3EKw5sX'
access_token_secret = 'BNvOIHoP10Hieto26Ts8lb0VAh4uLu3I3b2aRFNUXh8dW'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Add keywords for searching
search_words = "bed available"
date_since = "2021-04-27"

new_search = search_words + " -filter:retweets"


tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(20)


tweets = tw.Cursor(api.search, q=new_search,lang="en",since=date_since).items(20)

users_locs = [[tweet.user.location,tweet.text] for tweet in tweets]



tweet_text = pd.DataFrame(data=users_locs, columns=['Location',"Tweet"])
tweet_text.to_csv("information.csv",)

display(tweet_text)