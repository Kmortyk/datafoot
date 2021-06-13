import io
import os
from typing import List
from PIL import Image
from interfaces.writer import Writer
import stage


class WriteImageBytes(Writer):
    counter = 0

    def __init__(self, base_path, base_name='image', ext='jpg'):
        # create dir in advance to have opportunity to open file
        stage.CreateDir(base_path).execute()

        self.ext = ext
        self.base_path = base_path
        self.base_name = base_name

    def write(self, images_bts) -> List[str]:
        res = []

        self.counter += 1

        path = os.path.join(self.base_path, self.base_name + str(self.counter) + "." + self.ext)
        res.append(path)

        img = Image.open(io.BytesIO(images_bts))
        img.save(path)

        return res
