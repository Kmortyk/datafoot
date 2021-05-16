from typing import List

# Pipeline: process data in sequential order with given stages
# Example:
# Pipeline: Stage1 -> Stage2 -> Output
# Each stage processes full list of data
# May be very slow on a big sets of data
from dataset import Dataset
from interfaces.converter import Converter
from interfaces.writer import Writer


class Pipeline:
    def __init__(self, *stages):
        self.stages = stages
        self.level = 1

    def __call__(self, *args, **kwargs):
        self.execute(args)

    def log(self, idx, cur_stage):
        log = f"> stage {idx + 1}/{len(self.stages)} '{type(cur_stage).__name__}'"

        for i in range(self.level):
            log = "-" + log

        if idx > 0:
            print('\n' + log)
        else:
            print(log)

    def execute(self, args=None) -> List[str]:
        if len(self.stages) == 0:
            print("no stages were passed to execute")
            return []

        idx = 0

        while True:
            # if all stages are processed
            if idx >= len(self.stages):
                return []

            stage = self.stages[idx]
            self.log(idx, stage)

            if issubclass(type(stage), Converter):
                ds = Dataset()
                for arg in args:
                    ds.append_rows(stage.convert(arg))

                args = ds

                # for column_name in ds.column_names:
                #     idx += 1
                #     if idx >= len(self.stages):
                #         return []
                #
                #     data_arg = ds[column_name]
                #
                #     next_stage = self.stages[idx]
                #     next_stage.level = self.level + 1
                #     next_stage.execute(data_arg)
            elif issubclass(type(stage), Writer):
                res = []

                for arg in args:
                    res.append(*stage.write(arg))

                args = res
            else:
                args = stage.execute(args)

            # inc idx of stages
            idx += 1
