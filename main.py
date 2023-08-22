from PIL import Image

#pip install opencv-python
#python -m pip install Pillow

def convert_to_greyscale(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert to greyscale
    greyscale_img = img.convert('L')

    # Save the converted image
    greyscale_img.save(output_path)

    print(f"Image saved to {output_path}")


# Usage
image_path = "/Users/asc/Documents/Prompts/Icons/Push.png"
output_path = "/Users/asc/Documents/Prompts/Icons/PushG.png"
convert_to_greyscale(image_path, output_path)