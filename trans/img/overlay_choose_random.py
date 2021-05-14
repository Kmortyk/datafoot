import random
import cv2
from src.datafoot.multipath import MultiPath
from src.datafoot.multipath.transform.transform import Transform


class OverlayChooseRandom(Transform):
    def __init__(self, targets_paths):
        self.targets_paths = targets_paths

    @staticmethod
    def overlay(background, overlay, pos=(0, 0), scale=1):
        overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
        h, w, _ = overlay.shape  # Size of foreground
        rows, cols, _ = background.shape  # Size of background Image
        y, x = pos[0], pos[1]  # Position of foreground/overlayImage image

        # loop over all pixels and apply the blending equation
        for i in range(h):
            for j in range(w):
                if x + i >= rows or y + j >= cols:
                    continue
                alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
                background[x + i][y + j] = alpha * overlay[i][j] + (1 - alpha) * background[x + i][y + j].copy()

        return background

    def rand_target(self):
        trg = self.targets_paths[random.randint(0, len(self.targets_paths) - 1)]

        return trg, cv2.imread(trg, cv2.IMREAD_UNCHANGED)

    # returns:
    # 0 - image with overlay path
    # 1 - target overlay path
    # 2 - target overlay pos in form (x1, y1, x2, y2)
    def transform(self, arg) -> MultiPath:
        trg_path, trg = self.rand_target()

        img = cv2.imread(arg, cv2.IMREAD_UNCHANGED)
        if img.shape[2] != 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)

        offset_x = random.randint(0, img.shape[1] - trg.shape[1] - 1)
        offset_y = random.randint(0, img.shape[0] - trg.shape[0] - 1)

        img = self.overlay(img, trg, (offset_x, offset_y))
        cv2.imwrite(arg, img)

        m = MultiPath()
        m.append([arg])
        m.append([trg_path])
        m.append([(offset_x, offset_y, offset_x + trg.shape[1], offset_y + trg.shape[0])])

        return m
