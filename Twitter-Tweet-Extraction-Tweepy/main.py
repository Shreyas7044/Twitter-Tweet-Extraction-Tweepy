import tweepy

# ================================
# Twitter API Credentials
# ================================
# Replace the X's with your actual credentials
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def get_tweets(username, number_of_tweets=200):
    """
    Extract tweets from a given Twitter username.

    :param username: Twitter handle of the user
    :param number_of_tweets: Number of tweets to extract (max 3200)
    """

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Fetch tweets
    tweets = api.user_timeline(
        screen_name=username,
        count=number_of_tweets,
        tweet_mode="extended"
    )

    extracted_tweets = []

    for tweet in tweets:
        extracted_tweets.append(tweet.full_text)

    # Print tweets
    for idx, text in enumerate(extracted_tweets, start=1):
        print(f"{idx}. {text}\n")


if __name__ == "__main__":
    # Replace with the Twitter username you want to scrape
    get_tweets("twitter-handle")