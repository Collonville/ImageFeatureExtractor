import colour
import numpy as np


def to_2d_array(array: np.ndarray):
    dimension = len(array.shape)

    if dimension == 1:
        raise ValueError("Array dimension is 1. Set array more than 2 dimension.")
    elif dimension == 2:
        return array

    return array.reshape((array.shape[0] * array.shape[1], array.shape[-1]))


def convert_color_space_from_rgb(
    np_image: np.ndarray, dest_color_space: str
) -> np.ndarray:
    if dest_color_space == "RGB":
        return np_image
    elif dest_color_space == "HSV":
        return colour.RGB_to_HSV(np_image)
    elif dest_color_space == "HSL":
        return colour.RGB_to_HSL(np_image)
    elif dest_color_space == "CMY":
        return colour.RGB_to_CMY(np_image)
    else:
        raise ValueError("Undefined color space.")
