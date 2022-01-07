class DatasetRowsIterator:
    def __init__(self, ds):
        self.ds = ds
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter == len(self.ds.column_values[0]):
            raise StopIteration

        # create dataset that holds one row
        row = DatasetRow()

        # add values of one row to that dataset
        for idx, col in enumerate(self.ds.column_names):
            row[col] = self.ds.column_values[idx][self.iter]

        self.iter += 1

        return row

class DatasetRow:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return f"{self.data}"
