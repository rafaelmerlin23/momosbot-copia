from App.MemeBot import MemeBot
from App.MemeGenerator import MemeGenerator
from App.TweetManager import TweetManager
from App.resources.plantillas import plantillas
from resources.credentials import twitter_credentials  as t_c

if __name__ == "__main__":


     manager = TweetManager(
          api_key= str(t_c["api_key"])
          ,access_token= str(t_c["access_token"])
          ,bearer_token= str(t_c["bearer_token"])
          ,access_token_secret = str(t_c["access_token_secret"])
          ,api_key_secret= str(t_c["api_key_secret"])
     )

     generator = MemeGenerator(memes_path="memes/",images_path="imagenes/",templates=plantillas)

     bot = MemeBot(tweet_manager=manager,memes_path="memes/",images_path="imagenes/",templates=plantillas,reddit_manager=None)



