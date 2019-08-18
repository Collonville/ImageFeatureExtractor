import unittest

import numpy as np
from colour.utilities import filter_warnings

from ife.util.array import to_2d_array, convert_color_space_from_rgb


class Test2dArray(unittest.TestCase):
    def test_1dim(self) -> None:
        with self.assertRaises(ValueError):
            to_2d_array(np.arange(4.0))

    def test_2dim(self) -> None:
        expected = np.array([[0, 1, 2], [3, 4, 5]], np.float)
        actual = to_2d_array(np.arange(6.0).reshape(2, 3))

        np.testing.assert_array_equal(expected, actual)

    def test_3dim(self) -> None:
        expected = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]], np.float)
        actual = to_2d_array(np.arange(12.0).reshape(2, 2, 3))

        np.testing.assert_array_equal(expected, actual)


class TestColorConvertFromRGB(unittest.TestCase):
    def test_rgb_2_rgb(self) -> None:
        expected = np.array([0, 0, 0])
        actual = convert_color_space_from_rgb(np.array([0, 0, 0]), "RGB")

        np.testing.assert_array_equal(expected, actual)

        expected = np.array([0.2, 0.4, 0.8])
        actual = convert_color_space_from_rgb(np.array([0.2, 0.4, 0.8]), "RGB")

        np.testing.assert_array_equal(expected, actual)

    def test_rgb_2_hsv(self) -> None:
        filter_warnings(python_warnings=True)
        expected = np.array([0, 0, 0])
        actual = convert_color_space_from_rgb(np.array([0, 0, 0]), "HSV")

        np.testing.assert_array_almost_equal(expected, actual)

        expected = np.array([0.611, 0.75, 0.80])
        actual = convert_color_space_from_rgb(np.array([0.2, 0.4, 0.8]), "HSV")

        np.testing.assert_array_almost_equal(expected, actual, decimal=3)

    def test_rgb_2_hsl(self) -> None:
        pass

    def test_rgb_2_cmy(self) -> None:
        pass
