import cv2
import numpy as np

# Load the watermark and watermarked images
watermark = cv2.imread('watermark\jwb.png', cv2.IMREAD_GRAYSCALE)
watermarked = cv2.imread('watermark\imawat.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply template matching using the watermark image as the template
result = cv2.matchTemplate(watermarked, watermark, cv2.TM_CCOEFF_NORMED)

# Define a threshold value to determine if the watermark is present or not
threshold = 0.8

# Find the location(s) where the template matches the image above the threshold
locations = np.where(result >= threshold)
if locations[0].size > 0:
    print("Watermark found!")
else:
    print("Watermark not found.")
