import unittest
from collections import defaultdict

import numpy as np
import pandas as pd

from ife.io.io import ImageReader


class TestMomentFeatures(unittest.TestCase):
    def test_output_type(self) -> None:
        features = ImageReader.read_from_single_file("ife/data/small_rgb.jpg")

        moment = features.moment()
        self.assertIs(np.ndarray, type(moment))

        moment = features.moment(output_type="")
        self.assertIs(np.ndarray, type(moment))

        moment = features.moment(output_type="one_col")
        self.assertIs(np.ndarray, type(moment))
        self.assertEqual(np.zeros(15).shape, moment.shape)  # type: ignore

        moment = features.moment(output_type="dict")
        self.assertIs(defaultdict, type(moment))

        moment = features.moment(output_type="pandas")
        self.assertIs(pd.DataFrame, type(moment))
