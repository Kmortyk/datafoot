from dataset import Dataset


class PickColumns:
    def __init__(self, *column_names):
        self.column_names = column_names

    def execute(self, ds: Dataset) -> Dataset:
        print(f"pick columns '{self.column_names}'")

        new_ds = Dataset()

        for column_name in self.column_names:
            new_ds.append_column(column_name, ds[column_name])

        return new_ds
