from typing import List as PythonList


# list passed objects
# use for debug purpose


class List:
    def __init__(self, log_each=False):
        self.log_each = log_each

    def execute(self, args=None) -> PythonList[str]:
        if self.log_each:
            if len(args) == 0:
                print("nothing to list")
                return []

            for idx, arg in enumerate(args):
                print(f"[{idx}]: {arg}")
        else:
            print(f"listed {len(args)} objects")

        return args
