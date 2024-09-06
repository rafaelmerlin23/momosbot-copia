from http.client import responses

import praw
import requests
from App.Interfaces import ImagePoster


class RedditManager(ImagePoster):

    def __init__(self,client_id,client_secret,user_agent,username,password):
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__user_agent = user_agent
        self.__username = username
        self.__password = password

        self.__reddit = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            user_agent = user_agent,
            username = username,
            password = password
        )


    def post_image(self,image_path,text):
        print("se publicó el meme en reddit")


    def get_random_images(self, number_of_images, subreddit_name):
        print(f"{number_of_images} imagenes obtenidas de {subreddit_name}")

