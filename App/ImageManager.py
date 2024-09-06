from PIL import Image

from App.Interfaces import ImageScaler


class ImageManager(ImageScaler):


    @staticmethod
    def scale(dimensions_to_scale,image):
        scale_image = image.copy()
        return scale_image.resize(dimensions_to_scale)

    @staticmethod
    def scale_without_deforming(dimensions_to_scale,image):
        scale_image = image.copy()
        scale_image.thumbnail(dimensions_to_scale)
        return  scale_image

    @staticmethod
    def put_watermark(meme,water_mark):
        rescale_tuple = (meme.size[0]//6,meme.size[1]//6)
        scale_water_mark = ImageManager.scale_without_deforming(rescale_tuple,water_mark)

        scale_water_mark.putalpha(64)
        wm_w,wm_h = scale_water_mark.size
        bg_w,bg_h = meme.size

        offset = ((bg_w - wm_w)//2,(bg_h - wm_h) //2)
        meme.paste(scale_water_mark,offset,scale_water_mark)
