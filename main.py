from PIL import Image


def convert_to_greyscale(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert to greyscale
    greyscale_img = img.convert('L')

    # Save the converted image
    greyscale_img.save(output_path)

    print(f"Image saved to {output_path}")


# Usage
image_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\Home.png"
output_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\HomeGrey.png"
convert_to_greyscale(image_path, output_path)