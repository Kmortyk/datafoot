import os
from typing import List

import stage
from interfaces.writer import Writer
from writer import WriteImageBytes


class WriteTxtDatasetSample(Writer):
    counter = 0

    def __init__(self, output_path, txt_file_name='data'):
        # create dir in advance to have opportunity to open file
        stage.CreateDir(output_path).execute()

        self.output_path = output_path
        self.writer = WriteImageBytes(output_path)
        self.txt_file_name = txt_file_name
        self.f = open(os.path.join(self.output_path, self.txt_file_name + '.txt'), "a")

    def write(self, dss) -> List[str]:
        image_path = self.writer.write(dss["image_bytes"])[0]

        width = dss['width']
        height = dss['height']

        line = f"{image_path} {height} {width} "

        for idx in range(dss["bbox_count"]):
            xmin = int(dss['bbox_xmin_arr'][idx] * width)
            ymin = int(dss['bbox_ymin_arr'][idx] * height)
            xmax = int(dss['bbox_xmax_arr'][idx] * width)
            ymax = int(dss['bbox_ymax_arr'][idx] * height)

            # TODO do we need this?
            label_id = dss['labels_id'][idx] - 1

            line += f"{xmin} {ymin} {xmax} {ymax} {label_id} "

        line = line.strip()
        line += "\n"

        print(f"write to txt, path: '{self.output_path}' image:'{image_path}'")

        self.f.write(line)
        # self.f.close()

        # TODO return dataset
        return [image_path]
