from App.ImageManager import ImageManager


class Template:
    def __init__(self,place_images,template_image):
        self.__place_image = place_images
        self.__template_image = template_image


    def fill_template(self,images):
        filled_template = self.__template_image.copy()
        i = 0
        for place in self.__place_image:
            rescale_image = ImageManager.scale(place["scale"],images[i])
            filled_template.paste(rescale_image,place["location"])
            i+=1

        return filled_template


    def __len__(self):
       return  len(self.__place_image)

