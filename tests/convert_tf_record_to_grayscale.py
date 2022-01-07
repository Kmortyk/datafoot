import unittest

import convert
import reader.tf.tf_record_reader
import writer
from workflow import *


class TestPipeline(unittest.TestCase):
    def test_read_tf_record(self):
        # testing
        # training

        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/training.record'
        tf_output_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/grayscale/training_grayscale.record'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                convert.tf.TFRecordsToDataset(),
                convert.img.Grayscale(),
                # dataset.PrintDataset(),
                writer.WriteTFRecord(output_path=tf_output_path),
            ],
            batch_size=100
        )()


if __name__ == '__main__':
    unittest.main()
