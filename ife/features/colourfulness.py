import numpy as np


def colourfulness(np_2d_image: np.ndarray) -> np.float64:
    """
    Get colourfulness of the image

    Parameters
    ----------
    np_2d_image : np.ndarray
        RGB image array. Other colour space is not allowed.

    Returns
    ----------
    float
        Value of colourfulness.

    References
    ----------
    D. Hasler and S.E.Suesstrunk, ``Measuring colorfulness in natural images," Human
    Vision andElectronicImagingVIII, Proceedings of the SPIE, 5007:87-95, 2003.
    """
    rg = np_2d_image[:, 0] - np_2d_image[:, 1]
    yb = 0.5 * (np_2d_image[:, 0] + np_2d_image[:, 1]) - np_2d_image[:, 2]

    mean_rgyb = np.sqrt(np.mean(rg) ** 2 + np.mean(yb) ** 2)
    std_rgyb = np.sqrt(np.std(rg) ** 2 + np.std(yb) ** 2)

    return std_rgyb + 0.3 * mean_rgyb
