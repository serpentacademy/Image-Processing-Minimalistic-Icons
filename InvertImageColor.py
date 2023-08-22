import cv2

def invert_colors(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Read with the alpha channel (transparency)

    # Invert the image
    inverted_img = cv2.bitwise_not(img)

    # Save the inverted image
    cv2.imwrite(output_path, inverted_img)

# Usage
image_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\HomeGrey.png"
output_path = "C:\\Users\\neocr\\Documents\\Prompts\\Icons\\HomeGreyI.png"
invert_colors(image_path, output_path)