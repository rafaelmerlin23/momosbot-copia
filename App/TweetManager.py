from itertools import count

import tweepy
from App.Interfaces import ImagePoster, ImageFetcher
class TweetManager(ImagePoster):



    def __init__(self, api_key, api_key_secret, bearer_token, access_token, access_token_secret):

        self.__api_key = api_key
        self.__api_key_secret = api_key_secret
        self.__bearer_token = bearer_token
        self.__access_token = access_token
        self.__access_token_secret = access_token_secret

        auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        self._api = tweepy.API(auth, wait_on_rate_limit=True)

        self._client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )

    def post_text(self, text):
        self._client.create_tweet(text=text)
        print("Se ha twitteado.")

    def post_image(self, image_path, text):
        # Subir la imagen utilizando la API v1.1
        media = self._api.media_upload(image_path)
        media_id = media.media_id_string
        # Crear el tweet con la imagen utilizando la API v2
        self._client.create_tweet(text=text, media_ids=[media_id])
        print("Se ha twitteado con imagen.")




