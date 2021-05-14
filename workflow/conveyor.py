from typing import List

# Conveyor: process data in sequential order with given stages
# Example:
# Pipeline: Stage1 -> Stage2 -> Output
# Each stage processes full list of data
# May be very slow on a big sets of data
from workflow import Pipeline


class Conveyor:
    level = 1

    def __init__(self, reader, batch_size=10, *stages):
        self.stages = stages
        self.batch_size = batch_size
        self.reader = reader

    def __call__(self, *args, **kwargs): self.execute(args)

    def execute(self, args=None) -> List[str]:
        res = []

        while True:
            batch = []

            for _ in range(0, self.batch_size):
                item, stop = self.reader.read()
                if stop:
                    return res
                batch.append(item)

            res.append(*Pipeline(self.stages)(batch)())
