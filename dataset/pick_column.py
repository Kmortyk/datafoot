from typing import List

from dataset import Dataset


class PickColumn:
    def __init__(self, column_name):
        self.column_name = column_name

    def execute(self, ds: Dataset) -> List:
        return ds[self.column_name]
