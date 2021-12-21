import io
from PIL import Image
from dataset import Dataset
from interfaces.converter import Converter

class Grayscale(Converter):
    def __init__(self):
        pass

    def convert(self, ds) -> Dataset:
        images_bts = ds['image_bytes']
        img = Image.open(io.BytesIO(images_bts)).convert('L')

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')

        ds['image_bytes'] = [img_byte_arr.getvalue()]

        return ds