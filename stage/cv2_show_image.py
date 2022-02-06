import io
from typing import List, Optional
import cv2
import numpy as np
from PIL import Image

from dataset import Dataset

WINDOW_NAME = "stage.Cv2ShowImage"

class Cv2ShowImage:
    def __init__(self, return_if=None, draw_bboxes=False):
        self.return_if = return_if
        if self.return_if is None:
            self.return_if = lambda x: True
        self.draw_bboxes = draw_bboxes

    def execute(self, ds: Dataset) -> Optional[Dataset]:
        if len(ds['image_bytes'][0]) > 1:
            raise Exception("Cv2ShowImage: got more than 1 image")

        image_bytes = ds['image_bytes'][0][0]
        w = ds['width'][0][0]
        h = ds['height'][0][0]

        image = (np.array(Image.open(io.BytesIO(image_bytes)).convert('RGB')))[:, :, ::-1].copy()

        if self.draw_bboxes:
            count = ds['bbox_count'][0][0]
            for i in range(count):
                xmin = int(w*ds['bbox_xmin_arr'][0][0][i])
                ymin = int(h*ds['bbox_ymin_arr'][0][0][i])
                xmax = int(w*ds['bbox_xmax_arr'][0][0][i])
                ymax = int(h*ds['bbox_ymax_arr'][0][0][i])

                cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (255,255,255))

        cv2.imshow(WINDOW_NAME, image)

        if self.return_if(image_bytes):
            print("[INFO] Cv2ShowImage: image needs to be saved.")
            return ds
        else:
            return None
