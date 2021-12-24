import io
import os
from typing import List
from PIL import Image
from interfaces.writer import Writer
import stage
import tensorflow as tf

from writer.tf.tf_annot import TFAnnotation


class WriteTFRecord(Writer):
    counter = 0

    def __init__(self, output_path):
        stage.CreateDir(os.path.dirname(output_path)).execute() # create directory for the record
        self.output_path = output_path
        self.dataset_writer = tf.io.TFRecordWriter(output_path)

    def write(self, ds) -> List[str]:
        annot = TFAnnotation()

        # print(ds)
        # print("width height filename encoding image_bytes bbox_count bbox_xmin_arr bbox_xmax_arr bbox_ymin_arr bbox_ymax_arr labels labels_id difficult")
        # print(width, height, filename, encoding, image_bytes[:20], bbox_count, bbox_xmin_arr, bbox_xmax_arr, bbox_ymin_arr, bbox_ymax_arr, labels, labels_id, difficult)

        self.dataset_writer.write(annot.build_raw_serialized_example(
            ds["height"],
            ds["width"],
            ds["filename"],
            ds["image_bytes"],
            ds["encoding"],
            ds["bbox_xmin_arr"],
            ds["bbox_xmax_arr"],
            ds["bbox_ymin_arr"],
            ds["bbox_ymax_arr"],
            ds["labels"],
            ds["labels_id"],
            ds["difficult"]
        ))

        return [self.output_path]
