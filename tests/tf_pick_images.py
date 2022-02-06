import unittest
import convert
import dataset
import reader.tf.tf_record_reader
import stage
import writer
from workflow import *
import cv2

def need_save_action(image_bytes) -> bool:
    key = cv2.waitKey(0)

    if key == ord('s'):
        return True

    return False

class TestConveyor(unittest.TestCase):
    def test_read_tf_record(self):
        tf_record_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/testing.record'
        output_path = '/mnt/sda1/Projects/PycharmProjects/MikeHotel_TFOD2/dataset/bottle_soup_green/picked'

        imgs_path = output_path + '/img'
        csv_path = output_path + '/bboxes.csv'

        Conveyor(
            reader=reader.tf.TFRecordReader(tf_record_path),
            stages=[
                convert.tf.TFRecordsToDataset(),
                stage.Cv2ShowImage(return_if=need_save_action, draw_bboxes=True),
                writer.WritersMergePipelines(
                    Pipeline(
                        writer.WriteImageDataset(imgs_path),
                    ),
                    Pipeline(
                        dataset.PickColumns(
                            "filename", "bbox_count", "bbox_xmin_arr",
                            "bbox_ymin_arr", "bbox_xmax_arr", "bbox_ymax_arr",
                            "labels"),
                        writer.WriteCSVFile(csv_path, log=True, instant_flush=True),
                    ),
                ),
            ],
            batch_size=1
        )()


if __name__ == '__main__':
    unittest.main()
