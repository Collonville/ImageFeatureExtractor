from ife.io.io import ImageReader


def main():
    features = ImageReader.read_from_single_file("ife/data/strawberry.jpg")

    print(
        features.moment(
            methods=["var", "mean"], output_type="pandas", color_space="HSV"
        )
    )
    print(type(features.colourfulness(output_type="")))


if __name__ == "__main__":
    main()
