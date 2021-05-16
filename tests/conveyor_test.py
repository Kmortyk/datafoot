import unittest

import convert
import dataset
import reader.tf.tf_record_reader
import writer
from workflow import *


class TestPipeline(unittest.TestCase):
    def test_read_tf_record(self):
        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup/training.tfrecord'
        output_images = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/images'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                convert.tf.TFRecordsToDataset(),
                dataset.PickColumn("image_bytes"),
                writer.WriteImageBytes(base_path=output_images),
            ]
        )()

    def test_write_tf_record_labels_to_txt(self):
        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup/training.tfrecord'
        output_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/images'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                convert.tf.TFRecordsToDataset(),
                writer.WriteTxtDatasetSample(output_path=output_path)
            ]
        )()


if __name__ == '__main__':
    unittest.main()
