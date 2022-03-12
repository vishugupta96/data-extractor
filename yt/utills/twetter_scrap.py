import pandas as pd
import tweepy
import pprint
import json



def twetter_data_mine(data,screen):

    auth = tweepy.OAuthHandler(data.twitter_consumer_key, data.twitter_consumer_secret)
    auth.set_access_token(data.twitter_access_token, data.twitter_access_token_secret)
    api = tweepy.API(auth)

    print(screen)

    number_of_tweets  = 20
    tweets = []
    likes = []
    time = []
    source = []
    name = []
    followers_count = []
    friend_count = []
    listed_count = []
    retweets = []

    for i in tweepy.Cursor(api.user_timeline, screen_name = screen, tweet_mode = 'extended').items(number_of_tweets):
        tweets.append(i.full_text)
        likes.append(i.favorite_count)
        time.append(i.created_at)
        source.append(i.source)
        name.append(i.user.name)
        followers_count.append(i.user.followers_count)
        friend_count.append(i.user.friends_count)
        retweets.append(i.retweet_count)

    print('retweets=' , retweets)

    x = pd.DataFrame({'tweets':tweets,'likes':likes,'time':time,'source':source,'name':name,'followers_count':followers_count,'friend_count':friend_count ,'retweets':retweets})

    x.to_csv('static/file/twetter.csv' ,index = False)



    return(x)

# r = twetter_data_mine(data)





