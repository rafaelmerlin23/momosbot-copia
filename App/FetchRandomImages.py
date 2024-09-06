import os
from PIL import Image
import random

from App.Interfaces import ImageFetcher


class FetchRandomImages(ImageFetcher):
    def __init__(self):
        pass

    @staticmethod
    def get_random_images(number_of_images, path):
        images_path = os.listdir(path)
        images = []

        for i in range(number_of_images):
            image_name = random.choice(images_path)
            full_image_path = os.path.join(path, image_name)  # Se une el nombre del archivo con el path
            image = Image.open(full_image_path)
            images.append(image)


        return images