from collections import defaultdict
from typing import Optional, Union, List

import numpy as np
import pandas as pd

from ife.util.array import to_2d_array, convert_color_space_from_rgb
from . import moment, colourfulness


class Features:
    np_image: np.ndarray

    def __init__(self, np_image: np.ndarray) -> None:
        self.np_image = np_image

    def moment(
        self,
        methods: Optional[List[str]] = None,
        color_space: Optional[str] = None,
        output_type: Optional[str] = None,
    ) -> Union[np.ndarray, dict, pd.DataFrame]:
        color_space = "RGB" if color_space is None else color_space

        np_2d_image = convert_color_space_from_rgb(
            to_2d_array(self.np_image), color_space
        )

        moments, method_list = moment.get_moments(methods, np_2d_image)

        if output_type is None or output_type == "":
            return moments
        elif output_type == "one_col":
            return moments.flatten()

        dict_result = defaultdict(dict)  # type: defaultdict
        for method_idx, method in enumerate(method_list):
            for index in range(moments.shape[1]):
                dict_result[method][color_space[index]] = moments[method_idx, index]

        if output_type == "dict":
            return dict_result
        elif output_type == "pandas":
            return pd.DataFrame(dict_result)
        else:
            raise ValueError("Undefined output type.")

    def colourfulness(
        self, output_type: Optional[str] = None
    ) -> Union[np.float64, np.ndarray, dict, pd.DataFrame]:
        np_2d_image = to_2d_array(self.np_image)

        value = colourfulness.colourfulness(np_2d_image)

        if output_type is None or output_type == "" or output_type == "one_col":
            return value

        dict_result = {"colourfulness": value}

        if output_type == "dict":
            return dict_result
        elif output_type == "pandas":
            return pd.DataFrame(dict_result, index=["value"])
        else:
            raise ValueError("Undefined output type.")
