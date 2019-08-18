from ife.io.io import ImageReader


def main():
    features = ImageReader.read_from_single_file("ife/data/small_rgb.jpg")

    print(features.moment(methods=["var", "mean"], output_type="", color_space="HSV"))


if __name__ == "__main__":
    main()
