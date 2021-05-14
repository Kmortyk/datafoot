import os
import shutil
from typing import List


class CopyTo:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def execute(self, args=None) -> List[str]:
        files = []

        print(f"copy {len(args)} files to '{self.output_dir}'")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for path in args:
            files.append(shutil.copy2(path, self.output_dir))

        return files
