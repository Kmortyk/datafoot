from dataset import Dataset


# column_values_func must return list of column values
# example:
#
# from typing import List
#
# def column_values_func(ds: Dataset) -> List:
#     nums = ds["numbers"]
#     res = []
#
#     for i in range(len(nums)):
#         res.append(nums[i] + 1)
#
#     return res


class CreateColumnFunction:
    def __init__(self, column_name, column_values_func):
        self.column_name = column_name
        self.column_func = column_values_func

    def execute(self, original: Dataset) -> Dataset:
        column_values = self.column_func(original)

        result = Dataset()
        result.append_column(self.column_name, [column_values])

        return result
