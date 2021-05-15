import tensorflow as tf

from reader.tf.tf_record import TFRecord


class TFRecordReader:
    def __init__(self, path):
        self.dataset = tf.data.TFRecordDataset(path)
        self.iter = self.dataset.__iter__()

    def read(self) -> (TFRecord, bool):
        try:
            raw_record = next(self.iter)
        except StopIteration:
            return None, False

        record = TFRecord()
        record.parse_raw_record(raw_record)

        # print(record)

        return record, True
