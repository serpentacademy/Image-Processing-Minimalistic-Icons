import cv2
import numpy as np

#pip install opencv-contrib-python
def remove_light_background(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)

    # Convert image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define a mask using color thresholding
    lower_bound = np.array([0, 0, 130])  # Adjust these values based on the specific background color
    upper_bound = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Invert the mask to keep the foreground
    mask_inv = cv2.bitwise_not(mask)

    # Use the mask to extract the foreground
    foreground = cv2.bitwise_and(img, img, mask=mask_inv)

    # Convert black background to transparency (alpha channel)
    tmp = cv2.cvtColor(foreground, cv2.COLOR_BGR2BGRA)
    tmp[:, :, 3] = mask_inv

    # Save the output image
    cv2.imwrite(output_path, tmp)


# Usage
image_path = "/Users/asc/Documents/Prompts/Icons/Search_2GNOBG.png"
output_path = "/Users/asc/Documents/Prompts/Icons/Search_2GNOBGFinal.png"
remove_light_background(image_path, output_path)