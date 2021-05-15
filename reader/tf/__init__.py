import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # disable tf logs

from .tf_record_reader import TFRecordReader
