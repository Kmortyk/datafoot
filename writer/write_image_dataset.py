import io
import os
from typing import List
from PIL import Image

from dataset import Dataset
from interfaces.writer import Writer
import stage


class WriteImageDataset(Writer):
    counter = 0

    def __init__(self, base_path):
        # create dir in advance to have opportunity to open file
        stage.CreateDir(base_path).execute()

        self.base_path = base_path

    def write(self, ds: Dataset) -> List[str]:
        res = []

        path = os.path.join(self.base_path, ds['filename'][0][0].decode("utf-8"))
        res.append(path)

        image_bytes = ds['image_bytes'][0][0]

        img = Image.open(io.BytesIO(image_bytes))
        img.save(path)

        return res
