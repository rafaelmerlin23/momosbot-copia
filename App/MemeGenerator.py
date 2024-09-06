import random
from datetime import datetime

from PIL import Image

from App.FetchRandomImages import FetchRandomImages
from App.ImageManager import ImageManager
from App.Interfaces import ImageScaler


class MemeGenerator:
    templates = []
    __water_mark = Image.open("marca de agua.png")

    def __init__(self,templates,images_path,memes_path):
        self.templates = templates
        self.images_path = images_path
        self.memes_path = memes_path

    def generate_meme(self):
        template = random.choice(self.templates)
        meme = template.fill_template(FetchRandomImages.get_random_images(len(template),self.images_path))
        ImageManager.put_watermark(meme= meme, water_mark= self.__water_mark)
        return meme

    def generate_and_save_meme(self):
        meme = self.generate_meme()
        path = f"{self.memes_path}{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.jpg"
        meme.save(path)
        return path

