import os
from typing import List
from interfaces.writer import Writer
import stage
import tensorflow as tf

from writer.tf.tf_annot import TFAnnotation


class WriteTFRecord(Writer):
    def __init__(self, output_path):
        stage.CreateDir(os.path.dirname(output_path)).execute() # create directory for the record
        self.output_path = output_path
        self.dataset_writer = tf.io.TFRecordWriter(output_path)

    def write(self, ds) -> List[str]:
        annot = TFAnnotation()

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
