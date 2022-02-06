from typing import List
from interfaces.writer import Writer
from dataset import Dataset

class WritersMerge(Writer):
    def __init__(self, *writers):
        self.writers = writers

    def write(self, ds: Dataset) -> List[str]:
        res = []

        for writer in self.writers:
            res.append(writer.write(ds))

        return res

class WritersMergePipelines(Writer):
    def __init__(self, *pipelines):
        self.pipelines = pipelines

    def write(self, ds: Dataset):
        res = []

        for pipeline in self.pipelines:
            copy = Dataset()
            copy.append_dataset(ds)

            r = pipeline.call_unwrap(copy)
            if r is not None:
                res.append(*r)

        return res
