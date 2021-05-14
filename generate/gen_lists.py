from interfaces.transform import Transform
from multipath.multipath import MultiPath


class GenLists(Transform):
    def __init__(self, count=1, size=100, fill=0):
        self.count = count
        self.size = size
        self.fill = fill

    def execute(self, _=None) -> MultiPath:
        m = MultiPath()

        for _ in range(self.count):
            m.append([self.fill] * self.count)

        return m
