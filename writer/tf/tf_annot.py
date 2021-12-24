import io

import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
from .tf_features import *

class TFAnnotation:
    def __init__(self):
        # additional variables
        self.width = None
        self.height = None

        self.filename = None
        self.encoding = None
        self.image_bytes = None

        # bounding box + label lists
        self.x_min_arr = []
        self.x_max_arr = []
        self.y_min_arr = []
        self.y_max_arr = []

        self.labels = []
        self.labels_id = []
        self.difficult = []

    def parse_record(self, record):
        example = tf.train.Example()
        example.ParseFromString(record.numpy())
        features = example.features.feature

        # load image from record
        self.width = features['image/width'].int64_list.value[0]
        self.height = features['image/height'].int64_list.value[0]
        self.filename = features['image/filename'].bytes_list.value[0]
        self.encoding = features['image/format'].bytes_list.value[0]
        self.image_bytes = features['image/encoded'].bytes_list.value[0]
        self.x_min_arr.extend(features['image/object/bbox/xmin'].float_list.value)
        self.x_max_arr.extend(features['image/object/bbox/xmax'].float_list.value)
        self.y_min_arr.extend(features['image/object/bbox/ymin'].float_list.value)
        self.y_max_arr.extend(features['image/object/bbox/ymax'].float_list.value)
        self.labels.extend(features['image/object/class/text'].bytes_list.value)
        self.labels_id.extend(features['image/object/class/label'].int64_list.value)
        self.difficult.extend(features['image/object/difficult'].int64_list.value)

    def add_bbox(self, bbox, label, label_id, difficult=0):
        # TensorFlow assumes all bounding boxes are in the
        # range [0, 1] so we need to scale them
        x_min = bbox[0] / self.width
        y_min = bbox[1] / self.height
        x_max = bbox[2] / self.width
        y_max = bbox[3] / self.height

        self.x_min_arr.append(x_min)
        self.y_min_arr.append(y_min)
        self.x_max_arr.append(x_max)
        self.y_max_arr.append(y_max)
        self.labels.append(label.encode())
        self.labels_id.append(label_id)
        self.difficult.append(difficult)

    def bboxes_count(self):
        counts = [
            len(self.x_min_arr),
            len(self.y_min_arr),
            len(self.x_max_arr),
            len(self.y_max_arr)
        ]

        for i in range(0, len(counts)-1):
            if counts[i] != counts[i+1]:
                print(f"[ERROR] not all counts are equal: {counts[i]} vs {counts[i+1]}")

        return counts[0]

    def bboxes(self):
        bboxes_list = []

        for i in range(0, self.bboxes_count()):
            bboxes_list.append([self.x_min_arr[i], self.y_min_arr[i],
                                self.x_max_arr[i], self.y_max_arr[i]])

        return bboxes_list

    def set_meta(self, filename, encoding):
        self.filename = filename.encode("utf-8")
        self.encoding = encoding.encode("utf-8")

    def set_cv_image(self, cv_image):
        # set image
        image = cv2.cvtColor(cv_image, cv2.COLOR_RGBA2BGR)
        np_image_data = np.asarray(image)
        tensor = tf.image.encode_jpeg(np_image_data)
        self.image_bytes = tensor.numpy()
        # set size
        height, width, channels = image.shape
        self.width = width
        self.height = height

    def cv_image(self):
        image = (np.array(Image.open(io.BytesIO(self.image_bytes)).convert('RGB')))[:, :, ::-1].copy()
        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
        return image

    def build_serialized_example(self):
        return self.build_raw_serialized_example(
            self.height,
            self.width,
            self.filename,
            self.image_bytes,
            self.encoding,
            self.x_min_arr,
            self.x_max_arr,
            self.y_min_arr,
            self.y_max_arr,
            self.labels,
            self.labels_id,
            self.difficult
        )

    @staticmethod
    def build_raw_serialized_example(height, width, filename, encoded, format, xmin, xmax, ymin, ymax, text, label, difficult):
        data = {  # construct the TensorFlow-compitable data dictionary
            "image/height": int64_feature(height),
            "image/width": int64_feature(width),
            "image/filename": bytes_feature(filename),
            "image/encoded": bytes_feature(encoded),
            "image/format": bytes_feature(format),
            "image/object/bbox/xmin": float_list_feature(xmin),
            "image/object/bbox/xmax": float_list_feature(xmax),
            "image/object/bbox/ymin": float_list_feature(ymin),
            "image/object/bbox/ymax": float_list_feature(ymax),
            "image/object/class/text": bytes_list_feature(text),
            "image/object/class/label": int64_list_feature(label),
            "image/object/difficult": int64_list_feature(difficult)
        }

        features = tf.train.Features(feature=data)
        example = tf.train.Example(features=features)

        return example.SerializeToString()

    def __str__(self) -> str:
        return f"""features {{
    filename: {self.filename}
    width: {self.width}
    height: {self.height}
    format: {self.encoding}
    encoded: {len(self.image_bytes)} bytes
    x_min_arr: {self.x_min_arr}
    y_min_arr: {self.y_min_arr}
    x_max_arr: {self.x_max_arr}
    y_max_arr: {self.y_max_arr}
    labels: {self.labels}
    labels_id: {self.labels_id}
    difficult: {self.difficult}
}}    
        """