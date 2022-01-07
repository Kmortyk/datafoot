import os
from typing import List
from interfaces.writer import Writer
import stage
import csv
from dataset import Dataset

class WriteCSVFile(Writer):
    counter = 0

    def __init__(self, output_path):
        stage.CreateDir(os.path.dirname(output_path)).execute() # create directory for the record
        self.output_path = output_path
        self.header_wrote = False
        self.csv_writer = csv.writer(open(output_path, 'w+', newline=''))

    def write(self, ds: Dataset) -> List[str]:
        # write header
        if not self.header_wrote:
            self.csv_writer.writerow(ds.column_names)
            self.header_wrote = True

        # write values
        for row in ds:
            values = row.row_values(0)
            print(f"write csv record: {values}")
            self.csv_writer.writerow(values)

        return [self.output_path]
