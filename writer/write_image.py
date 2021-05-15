import os
from typing import List
from PIL import Image
from interfaces.writer import Writer


class WriteImage(Writer):
    counter = 0

    def __init__(self, base_path, ext='jpg'):
        self.ext = ext
        self.base_path = base_path

    def write(self, images_bts) -> List[str]:
        res = []

        for bts in images_bts:
            self.counter += 1

            path = os.path.join(self.base_path) + str(self.counter) + "." + self.ext
            res.append(path)

            img = Image.fromarray(bts, mode='RGB')
            img.save(path)

        return res
