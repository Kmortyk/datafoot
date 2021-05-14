from typing import List


class WriteToFile:
    def __init__(self, path):
        self.path = path

    def execute(self, args=None) -> List[str]:
        with open(self.path, "w+") as f:
            for a in args:
                f.write(a)
        f.close()

        return [self.path]
