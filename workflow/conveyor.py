from typing import List

# Conveyor: process data in sequential order with given stages
# Example:
# Conveyor: Stage1 -> Stage2 -> Output
# Each stage processes small amount of data with size 'batch_size'

from workflow import Pipeline

class Conveyor:
    level = 1

    def __init__(self, reader, stages, batch_size=10):
        self.stages = stages
        self.batch_size = batch_size
        self.reader = reader

    def __call__(self, *args, **kwargs): self.execute(args)

    def execute(self, args=None):
        res = []

        while True:
            batch = []

            for _ in range(0, self.batch_size):
                item, ok = self.reader.read()
                if not ok:
                    break
                batch.append(item)

            print(f"\n# Process batch with size '{len(batch)}'\n")

            if len(batch) > 0:
                r = Pipeline(
                    *self.stages
                )(*batch)

                if r is not None:
                    res.append(*r)
            else:
                return res
