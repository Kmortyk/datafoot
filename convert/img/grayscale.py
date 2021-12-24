import io
from PIL import Image
from dataset import Dataset
from interfaces.converter import Converter

class Grayscale(Converter):
    def __init__(self):
        pass

    def convert(self, ds) -> Dataset:
        print(ds)

        images_bts = ds['image_bytes'][0]
        img = Image.open(io.BytesIO(images_bts)).convert('L')

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')

        ds['image_bytes'] = [[img_byte_arr.getvalue()]]

        return ds
