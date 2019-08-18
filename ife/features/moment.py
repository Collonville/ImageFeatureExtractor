from typing import Optional, List, Tuple

import numpy as np
from scipy import stats


def get_moments(
    methods: Optional[List[str]], np_2d_image: np.ndarray
) -> Tuple[np.ndarray, List[str]]:
    if methods is None:
        methods = ["mean", "median", "var", "skew", "kurtosis"]

    moments = np.array([eval(method)(np_2d_image) for method in methods])

    return moments, methods


def mean(np_2d_image: np.ndarray) -> np.ndarray:
    return np.mean(np_2d_image, axis=0)


def median(np_2d_image: np.ndarray) -> np.ndarray:
    return np.median(np_2d_image, axis=0)


def var(np_2d_image: np.ndarray) -> np.ndarray:
    return np.var(np_2d_image, axis=0)


def skew(np_2d_image: np.ndarray) -> np.ndarray:
    return stats.skew(np_2d_image, axis=0)


def kurtosis(np_2d_image: np.ndarray) -> np.ndarray:
    return stats.kurtosis(np_2d_image, axis=0)
