import os
from typing import List
from file import VideoReader


class SplitVideos:
    def __init__(self, dir_name=None, width=1024, output_ext='jpg'):
        self.dir_name = dir_name
        self.width = width
        self.output_ext = output_ext

    def execute(self, args=None) -> List[str]:
        if not len(args):
            return []

        vr = VideoReader(width=self.width, output_ext=self.output_ext)

        output_dir = os.path.join(os.path.dirname(args[0]), self.dir_name)
        files = []

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for i, path in enumerate(args):
            print(f"split '{path}' ({i + 1}/{len(args)})")
            vr.open(path)

            while vr.has_frames:
                files.append(vr.save_frame(output_dir))
                vr.next_frame()

        return files
