from dataset import Dataset

class PickColumns:
    def __init__(self, *column_names):
        self.column_names = column_names

    def execute(self, ds: Dataset) -> Dataset:
        if ds is None:
            raise Exception("PickColumns: dataset is None")

        new_ds = Dataset()

        for column_name in self.column_names:
            if column_name not in ds.column_names:
                raise Exception(f"PickColumns: cant find column '{column_name}' in the given dataset (existing columns: {ds.column_names})")

            new_ds.append_column(column_name, ds[column_name])

        return new_ds
