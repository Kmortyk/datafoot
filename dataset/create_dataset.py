from dataset import Dataset


class CreateDataset:
    def __init__(self, *stages):
        self.stages = stages

    def execute(self, original: Dataset) -> Dataset:
        result = Dataset()

        for stage in self.stages:
            result.append_dataset(stage.execute(original))

        return result
