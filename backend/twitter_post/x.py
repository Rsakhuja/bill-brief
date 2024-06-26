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

def split_text_for_threads(file_name, text, max_length=280):
    """
    Splits a long text into smaller parts suitable for a Twitter thread.

    Args:
    - text (str): The text to split into threads.
    - max_length (int): Maximum length of each thread part (default is 280 characters, Twitter's current limit).

    Returns:
    - list of str: List of texts, each representing a part of the thread.
    """
    threads = []

    bill_introduction = f"This is the summary of Bill {file_name} ::: \n"
    text = bill_introduction + text
    words = text.split()
    current_part = ""

    for word in words:
        if len(current_part) + len(word) + 1 <= max_length-3:
            if current_part:
                current_part += " "
            current_part += word
        else:
            threads.append(current_part+'...')
            current_part = word

    if current_part:
        threads.append(current_part)


    print(f"\n\n\nThis is what the threads looks like :::: {threads} \n\n\n")

    return threads


def post_to_twitter(file_name, summary):
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

    # # Texts to be Tweeted as a Thread
    # tweets = [
    #     "Hey Twitter!",
    #     "This is a thread.",
    #     "Each tweet is a reply to the previous one.",
    #     "And this is the last tweet in the thread!"
    # ]

    # Post the first tweet
    tweets = split_text_for_threads(file_name, text=summary)
    response = client.create_tweet(text=tweets[0])
    tweet_id = response.data['id']


    # # Post the subsequent tweets in the thread
    for tweet in tweets[1:]:
        time.sleep(2)
        response = client.create_tweet(text=tweet, in_reply_to_tweet_id=tweet_id)
        tweet_id = response.data['id']

    print(f"\n\nThread tweeted successfully! {tweet_id}\n\n")

    return 