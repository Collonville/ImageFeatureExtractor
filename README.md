# Image Feature Extractor(IFE)
[![Coverage Status](https://coveralls.io/repos/github/Collonville/ImageFeatureExtractor/badge.svg)](https://coveralls.io/github/Collonville/ImageFeatureExtractor)
[![Build Status](https://travis-ci.org/Collonville/ImageFeatureExtractor.svg?branch=develop)](https://travis-ci.org/Collonville/ImageFeatureExtractor)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/115c65043153459cbfc5026ea53be08d)](https://www.codacy.com/app/Collonville/ImageFeatureExtractor?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Collonville/ImageFeatureExtractor&amp;utm_campaign=Badge_Grade)
[![PyPI version](https://badge.fury.io/py/ife.svg)](https://badge.fury.io/py/ife)

## What is this...
`IFE` is a package to get an image feature more easily for Python. It contains many kinds of feature extract algorithms.

## Insatall
   For the latest version are available using pip install.
```bash
pip install ife
```

## 1. Features
### Color Moment
-   Mean, Median, Variance, Skewness, Kurtosis of `RGB, HSV, HSL, CMY`

## 2. Examples
Import the basic image reader of IFE.
```python
from ife.io.io import ImageReader
```

### 2.1 Get Moment
Add a image file path to `read_from_single_file()`. This will return basic features class.

And now! You can get a RGB color moment feature from image!!
```python
>>> features = ImageReader.read_from_single_file("ife/data/small_rgb.jpg")
>>> features.moment()
array([[ 0.57745098,  0.52156863,  0.55980392],
       [ 0.58823529,  0.48823529,  0.54901961],
       [ 0.15220588,  0.12136101,  0.12380911],
       [-0.01944425,  0.18416571,  0.04508015],
       [-1.94196824, -1.55209335, -1.75586748]])
```

Also, you can get an `flatten vector, dictionary, or pandas`
```python
>>> features.moment(output_type="one_col")
array([ 0.57745098,  0.52156863,  0.55980392,  0.58823529,  0.48823529,
        0.54901961,  0.15220588,  0.12136101,  0.12380911, -0.01944425,
        0.18416571,  0.04508015, -1.94196824, -1.55209335, -1.75586748])

>>> features.moment(output_type="dict")
defaultdict(<class 'dict'>, {'mean': {'R': 0.57745098039215681, 'G': 0.52156862745098043, 'B': 0.55980392156862746}, 'median': {'R': 0.58823529411764708, 'G': 0.48823529411764705, 'B': 0.5490196078431373}, 'var': {'R': 0.15220588235294119, 'G': 0.12136101499423299, 'B': 0.12380911188004615}, 'skew': {'R': -0.019444250980856902, 'G': 0.18416570783012232, 'B': 0.045080152334687214}, 'kurtosis': {'R': -1.9419682406751135, 'G': -1.5520933544103905, 'B': -1.7558674751807395}})

>>> features.moment(output_type="pandas")
       mean    median       var      skew  kurtosis
R  0.577451  0.588235  0.152206 -0.019444 -1.941968
G  0.521569  0.488235  0.121361  0.184166 -1.552093
B  0.559804  0.549020  0.123809  0.045080 -1.755867
```

> No! I want a HSV Color space feature :(

It can set another color space! Default will be RGB.
```python
>>> features.moment(output_type="one_col", color_space="CMY")
array([ 0.42254902,  0.47843137,  0.44019608,  0.41176471,  0.51176471,
        0.45098039,  0.15220588,  0.12136101,  0.12380911,  0.01944425,
       -0.18416571, -0.04508015, -1.94196824, -1.55209335, -1.75586748])
       
>>> features.moment(output_type="dict", color_space="HSL")
defaultdict(<class 'dict'>, {'mean': {'H': 0.50798329143793874, 'S': 0.52775831413836383, 'L': 0.61421568627450984}, 'median': {'H': 0.51915637553935423, 'S': 0.62898601603182969, 'L': 0.52156862745098043}, 'var': {'H': 0.13290200013401141, 'S': 0.10239897927552907, 'L': 0.051550124951941563}, 'skew': {'H': -0.078898095002588917, 'S': -0.83203104238315984, 'L': 1.0202366337483093}, 'kurtosis': {'H': -1.2599104562470791, 'S': -0.87111810912637022, 'L': -0.7502836585891588}})

>>> features.moment(output_type="pandas", color_space="HSV")
       mean    median       var      skew  kurtosis
H  0.507983  0.519156  0.132902 -0.078898 -1.259910
S  0.595236  0.749543  0.122723 -1.028366 -0.768867
V  0.855882  0.864706  0.013867 -0.155656 -1.498179
```

## 3. Future work
### IO
-   Read from URL links
-   Read from Base64
-   Sliding window
-   Video files

### Color space
-   CMYK
-   CIE Lab
-   XYZ

### Features
-   Value normalize
-   Average Gradient
-   LBP
-   Histogram
-   Color harmony
-   Entropy
-   Brightness measure
-   Contrast measure
-   Saturation measure
-   Colourfulness
-   Naturalness
-   Color fidelity metric
-   Saliency map
-   Fisher vector
-   VGG16, 19 layer feature
-   and more...

## 4. Author
@Collonville

## 5. Licence
BSD-3-Clause
