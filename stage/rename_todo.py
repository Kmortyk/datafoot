import os
import shutil
from typing import List

# TODO need to be done

def add_prefix(name, prefix):
    return prefix + name

def add_suffix(name, suffix):
    return name + suffix

def remove_prefix(name, prefix):
    if name.startswith(prefix) and len(name) != len(prefix):
        return name[len(prefix):]
    return name

def remove_suffux(name: str, suffix):
    if name.endswith(suffix) and len(name) != len(suffix):
        return name[:-len(suffix)]


class Rename:
    def __init__(self, add_prefix=None, add_suffix=None, remove_prefix=None, remove_suffix=None, replace_str=None, replacement=None):
        self.add_prefix = add_prefix
        self.add_suffix = add_suffix
        self.remove_prefix = remove_prefix
        self.remove_suffix = remove_suffix
        self.replace_str = replace_str
        self.replacement = replacement

    def execute(self, args=None) -> List[str]:
        files = []

        print(f"copy {len(args)} files to '{self.output_dir}'")

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for path in args:
            files.append(shutil.copy2(path, self.output_dir))

        return files