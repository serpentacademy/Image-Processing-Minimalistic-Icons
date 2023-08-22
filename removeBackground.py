from PIL import Image


def remove_light_background(image_path, output_path, threshold=200):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    grey_img = img.convert("L")

    # Convert to binary image with thresholding
    mask = grey_img.point(lambda p: p < threshold and 255)

    # Paste the original image using the mask
    transparent_background = Image.new("RGBA", img.size, (0, 0, 0, 0))
    transparent_background.paste(img, (0, 0), mask=mask)

    # Save the output
    transparent_background.save(output_path, "PNG")

    print(f"Image saved to {output_path}")


# Usage
image_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\User_Final.png"
output_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\User_FinalNOBG.png"
remove_light_background(image_path, output_path)