from dataset import Dataset

# debug stage
class PrintDataset:
    def execute(self, ds: Dataset) -> Dataset:
        print(f"print dataset")

        print(ds)

        return ds
