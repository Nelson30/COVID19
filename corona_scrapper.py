import GetOldTweets3 as got
import datetime as dt
import pandas as pd

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('#coronavirus #costarica')\
                                           .setSince("2020-02-01")\
                                           .setUntil("2020-04-02")\
                                           .setMaxTweets(500)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

text_tweets = [[tweet.id, tweet.username, tweet.text, tweet.formatted_date,
                tweet.retweets, tweet.favorites, tweet.mentions, tweet.hashtags, tweet.urls] for tweet in tweets]

dataset = pd.DataFrame(data = text_tweets, columns = ["ID","Usuario", "Texto", "Fecha", "Num.Retweets", "Num.Favoritos", "Mentions", "Hashtags","URLs"])

dataset.to_csv('corona_scrappe3.csv', index=False, encoding='utf-8')

