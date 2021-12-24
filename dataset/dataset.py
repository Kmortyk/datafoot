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

    def __setitem__(self, key, value):
        idx = self.__column_idx(key)
        self.columns[idx] = value

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

        max_size = 30
        tail = "\n| "

        l = 1
        if isinstance(self.columns[0], collections.Sized):
            l = len(self.columns[0])

        s = f"Dataset[r{l}:c{len(self.column_names)}]{tail}"

        for row_idx in range(l):
            for col in self.columns:
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

