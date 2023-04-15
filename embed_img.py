from PIL import Image

# Define file paths
main_file = "C:/Users/Jawahar/Pictures/Camera Roll/IMG_3042.JPG"
logo_file = "images/logo.png"

# Open images with Pillow
img_main = Image.open(main_file)
img_logo = Image.open(logo_file)

# Get image sizes
img_main_width, img_main_height = img_main.size
img_logo_width, img_logo_height = img_logo.size

# Create blank Pillow image
img_result = Image.new("RGB", (img_main_width, img_main_height))

# Paste main image onto result image
img_result.paste(img_main, (0, 0))

# Paste logo image onto result image
img_result.paste(img_logo, (100, 100))

# Save result image
img_result.save("result_5.png")
