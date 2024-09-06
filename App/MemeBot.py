from App.Interfaces import ImagePoster
from App.MemeGenerator import MemeGenerator


class MemeBot:
    def __init__(self,tweet_manager,images_path,memes_path,templates,reddit_manager):
        self.__tweet_manager = tweet_manager
        self.__images_path = images_path
        self.__memes_path = memes_path
        self.__templates = templates
        self.__reddit_manager = reddit_manager

    def post_image_on_twitter(self):
        generator = MemeGenerator(memes_path=self.__memes_path,templates=self.__templates,images_path=self.__images_path)
        meme_path = generator.generate_and_save_meme()
        meme_name = meme_path[meme_path.rfind("/") + 1:meme_path.find(".jpng") - 3]
        self.__tweet_manager.post_image(image_path= meme_path,text = f"momo: {meme_name}" )

    def post_image_on_reddit(self):
        self.__reddit_manager.post_image()