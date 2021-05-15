from typing import List as PythonList


# list passed objects
# use for debug purpose


class List:
    def __init__(self, print_each=False):
        self.print_each = print_each

    def execute(self, args=None) -> PythonList[str]:
        if self.print_each:
            if len(args) == 0:
                print("nothing to list")
                return []

            for idx, arg in enumerate(args):
                print(f"[{idx}]: {arg}")
        else:
            print(f"listed {len(args)} objects")

        return args
