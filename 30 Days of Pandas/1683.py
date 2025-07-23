# https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Invalid Tweets

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets.content.str.len() > 15][['tweet_id']]

# By: Fernando Serra
# https://github.com/fernandosserra