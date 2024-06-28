from utils.utils import split_text_for_threads
import tweepy
from dotenv import load_dotenv
import time
import os


# Enter API tokens below
bearer_token = os.getenv('bearer_token')
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

def post_to_twitter(file_name, llm_response):
    # V1 Twitter API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # V2 Twitter API Authentication
    client = tweepy.Client(
        bearer_token,
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        wait_on_rate_limit=True,
    )

    # Post the first tweet
    tweets = split_text_for_threads(file_name, llm_response=llm_response)
    response = client.create_tweet(text=tweets[0])
    tweet_id = response.data['id']


    # # Post the subsequent tweets in the thread
    for tweet in tweets[1:]:
        time.sleep(2)
        response = client.create_tweet(text=tweet, in_reply_to_tweet_id=tweet_id)
        tweet_id = response.data['id']

    print(f"\n\nThread tweeted successfully! {tweet_id}\n\n")

    return 