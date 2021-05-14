"""
    Reads video frame by frame.
"""

import imutils
import cv2
import os


class VideoReader:
    def __init__(self, frame_rate=0.5, width=1024, output_ext=".jpg"):
        self.frame_rate = frame_rate
        self.has_frames = False
        self.width = width
        self.ext = output_ext
        self.file_name = None
        self.cur_frame = None
        self.capt = None
        self.sec = 0

    def open(self, path):
        self.file_name = path.split(os.sep)[-1].split(".")[0]
        self.capt = cv2.VideoCapture(path)
        self.sec = 0
        # read one frame
        self.next_frame()

    def next_frame(self):
        (success, image) = self.__get_frame()
        self.has_frames = success
        self.cur_frame = image
        # calculate next frame position
        self.sec = round(self.sec + self.frame_rate, 2)
        return image

    # save image to the output directory
    def save_frame(self, output_dir):
        path = output_dir + os.sep + self.file_name + "_" + str(self.sec) + "." + self.ext
        cv2.imwrite(path, self.cur_frame)
        return path

    def get_frame(self):
        return self.cur_frame

    # get frame at concrete time position
    def __get_frame(self):
        self.capt.set(cv2.CAP_PROP_POS_MSEC, self.sec * 1000)
        has_frames, image = self.capt.read()
        if has_frames:
            image = imutils.resize(image, self.width)
        return has_frames, image
