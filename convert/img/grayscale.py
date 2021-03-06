import io
from PIL import Image
from dataset import Dataset
from interfaces.converter import Converter

class Grayscale(Converter):
    def __init__(self):
        pass

    def convert(self, ds) -> Dataset:
        images_bts = ds['image_bytes'][0]
        img = Image.open(io.BytesIO(images_bts)).convert('L')

        rgbimg = Image.new("RGB", img.size)
        rgbimg.paste(img)

        img_byte_arr = io.BytesIO()
        rgbimg.save(img_byte_arr, format='JPEG')

        ds['image_bytes'] = [img_byte_arr.getvalue()]

        return ds
