import os
from typing import List


class ListFiles:
    def __init__(self, path=None, formats=None):
        self.path = path
        self.formats = formats

    def execute(self, args=None) -> List[str]:
        results = []

        if len(args) > 0:
            print(f"listed {len(args)} files")
            return args

        if self.path is None:
            print(f"no path to list")
            return []

        for filename in os.listdir(self.path):
            extension = os.path.splitext(filename)[1].replace('.', '').lower()
            if self.formats is None or extension in self.formats:
                path = os.path.join(self.path, filename)
                results.append(path)

        print(f"listed {len(results)} files")

        return results
