import io
import os
from typing import List
from PIL import Image
from interfaces.writer import Writer
import stage

# todo this

class WriteTFRecord(Writer):
    counter = 0

    def __init__(self, output_path):
        stage.CreateDir(os.path.dirname(output_path)).execute() # create directory for the record
        self.output_path = output_path

    def write(self, ds) -> List[str]:
        print(ds)

        #
        # self.counter += 1
        # path = os.path.join(self.base_path, self.base_name + str(self.counter) + "." + self.ext)
        # res.append(path)
        # img = Image.open(io.BytesIO(ds))
        # img.save(path)
        #

        return [self.output_path]
