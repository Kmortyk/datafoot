from typing import List, Any

from dataset import Dataset


class AppendColumn:
    def __init__(self, dataset_reader, column_name: str, column_reader: List[Any]):
        self.dataset_reader = dataset_reader
        self.column_name = column_name
        self.column_reader = column_reader

    def execute(self, args) -> Dataset:
        print(f"append column '{self.column_name}'")



        self.dataset.append_column(self.column_name, self.column)

        return self.dataset
