import unittest

import stage
from workflow import Pipeline
import generate


class TestStages(unittest.TestCase):

    def test_list(self):
        Pipeline(
            generate.GenLists(3, size=10, fill=42),
            stage.List(print_each=True),
            stage.List(),
            stage.List()
        )()


if __name__ == '__main__':
    unittest.main()
