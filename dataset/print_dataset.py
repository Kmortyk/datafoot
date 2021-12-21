from dataset import Dataset

# debug stage
class PrintDataset:
    def execute(self, ds: Dataset) -> Dataset:
        print(f"print dataset")

        for column_name in ds.column_names:
            print(column_name)

        return ds
