# Twitter api
import tweepy
import os

def main():
    # Auth vars
    consumer_key = os.getenv('twitter_consumer_key')
    consumer_secret = os.getenv('twitter_consumer_secret')
    bearer_token = os.getenv('twitter_bearer_token')
    access_token = os.getenv('twitter_access_token')
    access_token_secret = os.getenv('twitter_access_token_secret')

    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Set text and image
    message = 'I wrote some simple code that posted this tweet. #python #tweepy'
    image = api.media_upload('image.jpg')

    # Post tweet with image
    api.update_status(status = message, media_ids=[image.media_id])

if __name__ == "__main__":
    main()