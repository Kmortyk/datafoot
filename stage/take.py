from typing import List


class Take:
    def __init__(self, count):
        self.count = count

    def execute(self, args=None) -> List[str]:
        if len(args) <= self.count:
            return args

        return args[:self.count]
