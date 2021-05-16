import hashlib
from typing import List


class ListWithSameContent:
    def __init__(self):
        pass

    def execute(self, args=None) -> List[str]:
        same_dict = {}

        if len(args) == 0:
            print(f"no files to list")
            return args

        for filepath in args:
            f = open(filepath, "rb")
            data = f.read()  # read binary
            f.close()

            h = hashlib.new('sha512')
            h.update(data)

            key = h.hexdigest()
            arr = same_dict.get(key)
            if arr is None:
                arr = []

            arr.append(filepath)
            same_dict[key] = arr

        find_at_least = False

        for k, arr in same_dict.items():
            if len(arr) > 1:
                find_at_least = True
                print(f"files {arr} are same")

        if not find_at_least:
            print("there's no exact files in directory")

        return args