"""
    Copies the most dissimilar images (by threshold value)
    to a separate folder.
"""
import os
from typing import List

import cv2


class Comparator:
    def __init__(self, method):
        self.method = method

    def compare(self, i, j):
        if self.method == "hist":
            return self.__compare_hist(i, j)
        elif self.method == "template":
            return self.__compare_template(i, j)

    @staticmethod
    def __compare_hist(i, j):
        hist_i = cv2.calcHist([i], [0], None, [256], [0, 256])
        hist_j = cv2.calcHist([j], [0], None, [256], [0, 256])
        return cv2.compareHist(hist_i, hist_j, cv2.HISTCMP_CORREL)

    @staticmethod
    def __compare_template(i, j):
        return cv2.matchTemplate(i, j, cv2.TM_CCOEFF_NORMED)[0][0]


class RemoveSimilarImages:
    def __init__(self, threshold=0.9, log_rate=1000):
        self.threshold = threshold
        self.log_rate = log_rate

    def execute(self, args=None) -> List[str]:
        if args is None:
            return []

        comp = Comparator("template")
        to_del = []
        files = []

        # for each two files
        for i in range(0, len(args) - 1):
            im_one = cv2.imread(args[i])
            im_two = cv2.imread(args[i + 1])

            eq = comp.compare(im_one, im_two)

            if i == 0 or (i + 1) % self.log_rate == 0:
                print(f"{len(to_del)} files will be removed ({i + 1}/{len(args) - 1})")

            if eq >= self.threshold:
                to_del.append(args[i])
            else:
                files.append(args[i])

        for i, d in enumerate(to_del):
            print(f"delete ({i + 1}/{len(to_del) - 1})")
            os.remove(d)

        return files
