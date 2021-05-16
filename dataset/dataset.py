import collections


class Dataset:
    iter = 0

    def __init__(self):
        self.columns = []
        self.column_names = []

    def append_column(self, column_name, column_data):
        self.columns.append(column_data)
        self.column_names.append(column_name)

    def append_rows(self, ds):
        # empty dataset case
        if len(self.column_names) != len(ds.column_names):
            self.column_names = ds.column_names
            self.columns = []
            for i in range(len(ds.column_names)):
                self.columns.append([])

        for ci, col in enumerate(ds.columns):
            self.columns[ci].append(*col)

    def __column_idx(self, name):
        for idx, col_name in enumerate(self.column_names):
            if col_name == name:
                return idx
        return -1

    def __getitem__(self, key):
        idx = self.__column_idx(key)
        return self.columns[idx]

    def __len__(self):
        return len(self.columns)

    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if self.iter == len(self.columns[0]):
            raise StopIteration

        ds = Dataset()

        for idx, col in enumerate(self.column_names):
            ds.append_column(col, self.columns[idx][self.iter])

        self.iter += 1

        return ds

    def __str__(self):
        if len(self.column_names) == 0:
            return "Dataset[r0:c0]"

        max_size = 10
        tail = "\n| "
        s = f"Dataset[r{len(self.columns[0])}:c{len(self.column_names)}]{tail}"

        for row_idx in range(len(self.columns[0])):
            for col in self.columns:
                v = col[row_idx]
                if isinstance(v, collections.Sized) and len(v) > max_size:
                    s += str(col[row_idx][:max_size]) + "... | "
                else:
                    s += str(col[row_idx]) + " | "
            if row_idx != len(self.columns[0]) - 1:
                s += tail

        return s

