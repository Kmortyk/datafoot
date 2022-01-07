import collections
from typing import List
from dataset.dataset_row import DatasetRowsIterator


class DatasetIterator:
    def __init__(self, ds):
        self.ds = ds
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter == len(self.ds.column_values[0]):
            raise StopIteration

        # create dataset that holds one row
        ds = Dataset()

        # add values of one row to that dataset
        for idx, col in enumerate(self.ds.column_names):
            ds.append_column(col, self.ds.column_values[idx][self.iter])

        self.iter += 1

        return ds

class Dataset:
    def __init__(self):
        self.column_values = []
        self.column_names = []

    def append_dataset(self, ds):
        for idx in range(len(ds)):
            column_name = ds.column_names[idx]
            column_value = ds.column_values[idx]

            if column_name in self.column_names:
                self.column_values[self.__column_idx(column_name)].append(column_value)
            else:
                self.append_column(column_name, column_value)

    def append_column(self, column_name, column_data):
        self.column_values.append(column_data)
        self.column_names.append(column_name)

    def append_rows(self, ds):
        # empty dataset case
        if len(self.column_names) != len(ds.column_names):
            # copy column names of merging dataset
            self.column_names = ds.column_names
            # initialize values as empty list
            self.column_values = []
            # initialize each column as empty list
            for i in range(len(ds.column_names)):
                self.column_values.append([])

        # todo add column names check

        # merge actual values to the current dataset
        for ci, col in enumerate(ds.column_values):
            self.column_values[ci].append(*col)

    def row_values(self, row_idx) -> List:
        result = []

        for col_idx in range(self.__len__()):
            result.append(self.column_values[col_idx][row_idx])

        return result

    def __column_idx(self, name):
        for idx, col_name in enumerate(self.column_names):
            if col_name == name:
                return idx

        # log error
        cols_log = f"{self.column_names[:100]}"
        if len(self.column_names) > 100:
            cols_log += "..."

        raise IndexError(f"not found '{name}', "
                         f"column names: {cols_log}")

    def __getitem__(self, key):
        return self.column_values[self.__column_idx(key)]

    def __setitem__(self, key, value):
        self.column_values[self.__column_idx(key)] = value

    def __len__(self):
        return len(self.column_values)

    def __iter__(self):
        return DatasetIterator(self)

    def rows(self):
        return DatasetRowsIterator(self)

    def __str__(self):
        if len(self.column_names) == 0:
            return "Dataset[r0:c0]"

        max_size = 45
        tail = "\n| "

        l = 1
        if isinstance(self.column_values[0], collections.Sized):
            l = len(self.column_values[0])

        s = f"Dataset[r{l}:c{len(self.column_names)}]{tail}"

        for row_idx in range(l):
            for col in self.column_values:
                if l == 1:
                    v = str(col)
                else:
                    v = str(col[row_idx])

                if isinstance(v, collections.Sized) and len(v) > max_size:
                    s += v[:max_size] + "... | "
                else:
                    s += v + " | "

            if row_idx != l - 1:
                s += tail

        return s

