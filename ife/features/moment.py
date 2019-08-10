from typing import Optional, Union

import numpy as np
from scipy import stats


def get_method(method: Optional[Union[str, list]] = None):
    if method is None:
        return MOMENT_METHODS.values()
    else:
        return [MOMENT_METHODS[method_name] for method_name in [method]]


def mean(np_2d_image: np.ndarray):
    return np.mean(np_2d_image, axis=0)


def median(np_2d_image: np.ndarray):
    return np.median(np_2d_image, axis=0)


def var(np_2d_image: np.ndarray):
    return np.var(np_2d_image, axis=0)


def skew(np_2d_image: np.ndarray):
    return stats.skew(np_2d_image, axis=0)


def kurtosis(np_2d_image: np.ndarray):
    return stats.kurtosis(np_2d_image, axis=0)


MOMENT_METHODS = {
    "Mean": mean,
    "Median": median,
    "Var": var,
    "Skew": skew,
    "kurtosis": kurtosis,
}
