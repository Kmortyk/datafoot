class MultiPath:
    def __init__(self):
        self.count = 0
        self.datas = []

    def append(self, data):
        self.count += 1
        self.datas.append(data)

    def merge(self, mp):
        self.count = mp.count
        if len(self.datas) < self.count:
            self.datas = []
            for i in range(self.count):
                self.datas.append([])

        for i, d in enumerate(mp.datas):
            self.datas[i].append(*d)

    def __getitem__(self, key):
        return self.datas[key]

    def __len__(self):
        return len(self.datas)

    def __iter__(self):
        return self.datas.__iter__()
