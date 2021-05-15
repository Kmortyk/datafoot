from dataset import Dataset


class GenLists:
    def __init__(self, count=1, size=100, fill=0):
        self.count = count
        self.size = size
        self.fill = fill

    def execute(self, _=None) -> Dataset:
        ds = Dataset()

        for idx in range(self.count):
            ds.append_column(str(idx), [self.fill] * self.size)

        return ds
