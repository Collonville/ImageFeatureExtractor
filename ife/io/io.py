import os

import numpy as np
from PIL import Image

from ife.features.features import Features


class ImageReader:
    def __init__(self):
        None

    @classmethod
    def read_from_single_file(cls, file_path: str) -> Features:
        if not isinstance(file_path, str):
            raise ValueError("Set string or list file path.")

        if not os.path.exists(file_path):
            raise FileExistsError("File {} does not exist.".format(file_path))

        np_image = np.array(Image.open(file_path).convert("RGB")) / 255.0

        return Features(np_image)
