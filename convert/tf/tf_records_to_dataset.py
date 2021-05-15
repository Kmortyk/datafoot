from dataset import Dataset
from interfaces.converter import Converter
from reader.tf.tf_record import TFRecord


class TFRecordsToDataset(Converter):
    def convert(self, record: TFRecord) -> Dataset:
        ds = Dataset()

        ds.append_column("width", [record.width])
        ds.append_column("height", [record.height])
        ds.append_column("filename", [record.filename])
        ds.append_column("encoding", [record.encoding])
        ds.append_column("image_bytes", [record.image_bytes])

        # TODO
        # ds.append_column("bbox_xmin_arr", record.x_min_arr)
        # ds.append_column("bbox_xmax_arr", record.filename)
        # ds.append_column("bbox_ymin_arr", record.filename)
        # ds.append_column("bbox_ymax_arr", record.filename)
        # ds.append_column("labels", record.filename)
        # ds.append_column("labels_id", record.filename)
        # ds.append_column("difficult", record.filename)

        return ds
