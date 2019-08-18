from ife.io.io import ImageReader


def main():
    features = ImageReader.read_from_single_file("ife/data/small_rgb.jpg")

    print(
        features.moment(
            required_methods=["var", "mean"], output_type="one_col", color_space="HSV"
        )
    )


if __name__ == "__main__":
    main()
