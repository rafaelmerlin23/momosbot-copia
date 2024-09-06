from abc import ABC,abstractmethod


class ImageScaler(ABC):

    @staticmethod
    @abstractmethod
    def scale(dimensions_to_scale,image):
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def scale_without_deforming(dimensions_to_scale, image):
        raise  NotImplementedError


class ImageFetcher(ABC):

    @staticmethod
    @abstractmethod
    def get_random_images(number_of_images,path):
        raise NotImplementedError


class ImagePoster(ABC):
    @abstractmethod
    def post_image(self,image_path,text):
        raise NotImplementedError

