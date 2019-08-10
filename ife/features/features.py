from collections import defaultdict

import numpy as np
import pandas as pd

from typing import Optional, Union

from ife.util.array import to_2d_array, convert_color_space_from_rgb
from . import moment


class Features:
    np_image: np.ndarray

    def __init__(self, np_image):
        self.np_image = np_image

    def moment(
        self,
        required_methods: Optional[Union[str, list]] = None,
        color_space: Optional[str] = "RGB",
        output_type: Optional[str] = None,
    ):
        np_2d_image = convert_color_space_from_rgb(
            to_2d_array(self.np_image), color_space
        )

        method_list = moment.get_method(required_methods)

        moment_value = np.array([method(np_2d_image) for method in method_list])

        if output_type is None or output_type is "":
            return moment_value
        elif output_type == "one_col":
            return moment_value.flatten()

        dict_result = defaultdict(dict)
        for method_idx, method in enumerate(method_list):
            for index in range(moment_value.shape[1]):
                dict_result[method.__name__][color_space[index]] = moment_value[
                    method_idx, index
                ]

        if output_type == "dict":
            return dict_result
        elif output_type == "pandas":
            return pd.DataFrame(dict_result)
        else:
            raise ValueError("Undefined output type.")
