from typing import List
from dataset import Dataset

class PickColumnAsDataset:
    def __init__(self, column_name):
        self.column_name = column_name

    def execute(self, original: Dataset) -> Dataset:
        print(f"pick column '{self.column_name}'")

        ds = Dataset()
        ds.append_column(self.column_name, original[self.column_name])

        return ds


class PickColumn:
    def __init__(self, column_name):
        self.column_name = column_name

    def execute(self, ds: Dataset) -> List:
        print(f"pick column '{self.column_name}'")

        return ds[self.column_name]
