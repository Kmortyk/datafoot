import unittest

import reader.tf.tf_record_reader
import stage
from workflow import *


class TestPipeline(unittest.TestCase):
    def test_read_tf_record(self):
        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup/training.tfrecord'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                stage.List(),
            ]
        )()


if __name__ == '__main__':
    unittest.main()
