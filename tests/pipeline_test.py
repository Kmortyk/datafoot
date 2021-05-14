import unittest

import stage
from workflow import Pipeline
import generate


class TestStages(unittest.TestCase):

    def test_list(self):
        Pipeline(
            generate.GenLists(3, size=90),
            stage.List(),
            stage.List(),
            stage.List()
        )()


if __name__ == '__main__':
    unittest.main()
