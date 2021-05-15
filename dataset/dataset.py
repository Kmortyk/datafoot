class Dataset:
    def __init__(self):
        self.columns_count = 0
        self.columns = []

    def append_column(self, data):
        self.columns_count += 1
        self.columns.append(data)

    def append_rows(self, ds):
        self.columns_count = ds.columns_count

        # empty dataset case
        if len(self.columns) < self.columns_count:
            self.columns = []
            for i in range(self.columns_count):
                self.columns.append([])

        for ci, col in enumerate(ds.columns):
            self.columns[ci].append(*col)

    def __getitem__(self, key):
        return self.columns[key]

    def __len__(self):
        return len(self.columns)

    def __iter__(self):
        return self.columns.__iter__()

    def __str__(self):
        if self.columns_count == 0:
            return "Dataset[r0:c0]"

        tail = "\n| "
        s = f"Dataset[r{len(self.columns[0])}:c{self.columns_count}]{tail}"

        for row_idx in range(len(self.columns[0])):
            for col in self.columns:
                s += str(col[row_idx]) + " | "
            if row_idx != len(self.columns[0]) - 1:
                s += tail

        return s

