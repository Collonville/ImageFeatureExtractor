import unittest

from ife.io.io import ImageReader, Features


class TestIO(unittest.TestCase):
    def test_undefined_type(self):
        with self.assertRaises(ValueError):
            ImageReader().read_from_single_file(["", ""])

    def test_unreachable_file(self):
        with self.assertRaises(FileExistsError):
            ImageReader().read_from_single_file("../../data/none")

    def test_reachable_file(self):
        expected = Features
        actual = ImageReader().read_from_single_file("ife/data/small_rgb.jpg")

        self.assertIs(expected, type(actual))
