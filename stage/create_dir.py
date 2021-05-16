import os
from typing import List


class CreateDir:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def execute(self, _=None) -> List[str]:
        print(f"create dir '{self.dir_path}'")

        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        return [self.dir_path]
