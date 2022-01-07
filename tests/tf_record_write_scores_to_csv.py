import math
import unittest

import convert
import reader.tf.tf_record_reader
import writer
import dataset
from workflow import *

# returns score with the given record
def get_scores(record_ds):
    scores = []

    for row in record_ds.rows():
        score = 0

        # img size
        w, h = row["width"][0], row["height"][0]

        img_area = w*h
        cx = 0 + w / 2
        cy = 0 + h / 2

        for bbox_idx in range(len(row["bbox_count"])):
            x_min = row["bbox_xmin_arr"][bbox_idx][0]
            y_min = row["bbox_ymin_arr"][bbox_idx][0]
            x_max = row["bbox_xmax_arr"][bbox_idx][0]
            y_max = row["bbox_ymax_arr"][bbox_idx][0]

            bbox_w = x_max - x_min
            bbox_h = y_max - y_min

            assert bbox_w > 0
            assert bbox_h > 0

            bbox_area = bbox_w * bbox_h
            bbox_cx = x_min + bbox_w / 2
            bbox_cy = y_min + bbox_h / 2

            assert bbox_area > 0

            # bounding box overall size
            area_frac = img_area / bbox_area

            # center point delta
            center_delta = math.sqrt((cx - bbox_cx)**2 + (cy - bbox_cy)**2)

            score += (50*area_frac + 50*center_delta)

        scores.append([score])

    return scores

def get_filename(record_ds):
    names = []

    for row in record_ds.rows():
        names.append([row["filename"][0].decode("utf-8")])

    return names

class TestConveyor(unittest.TestCase):
    def test_read_tf_record(self):
        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/training.record'
        csv_output_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/training_scores.csv'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                convert.tf.TFRecordsToDataset(),
                dataset.CreateDataset(
                    dataset.CreateColumnFunction("filename", get_filename),
                    dataset.CreateColumnFunction("score", get_scores),
                ),
                writer.WriteCSVFile(output_path=csv_output_path),
            ],
            batch_size=100
        )()


if __name__ == '__main__':
    unittest.main()
