import unittest

import stage
from workflow import Pipeline
import generate


class TestPipeline(unittest.TestCase):

    def test_gen_lists(self):
        Pipeline(
            generate.GenLists(3, size=10, fill=42),
            stage.List(print_each=True),
            stage.List(),
            stage.List()
        )()

    def test_list_with_same_content(self):
        Pipeline(
           stage.ListFiles("/home/kmortyk/Projects/ethp2p/sentry/testdata"),
           stage.ListWithSameContent()
        )()


if __name__ == '__main__':
    unittest.main()
