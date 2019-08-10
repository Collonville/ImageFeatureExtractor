from ife.io.io import ImageReader


def main():
    features = ImageReader.read_from_single_file("ife/data/small_rgb.jpg")

    print(features.moment(output_type="pandas"))


if __name__ == "__main__":
    main()
