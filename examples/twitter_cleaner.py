from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from cleaner import JsonCleaner
from auth_credentials import consumer_key, consumer_secret, access_token, access_token_secret


class TwitterStreamer(StreamListener):

    def on_data(self, raw_data):
        print raw_data

    def on_error(self, status_code):
        print status_code



if __name__ == '__main__':
    streamer = TwitterStreamer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, streamer)
    stream.filter(track=['messi, ronaldo, hazard'])