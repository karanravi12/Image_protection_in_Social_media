from PIL import Image, ImageEnhance

# Define file paths
watermarked_file = "images/jawa.png"
logo_file = "images/logo.png"

# Open images with Pillow
img_watermarked = Image.open(watermarked_file)
img_logo = Image.open(logo_file)

# Get image sizes
img_watermarked_width, img_watermarked_height = img_watermarked.size
img_logo_width, img_logo_height = img_logo.size

# Create blank Pillow image
img_result = Image.new("RGB", (img_watermarked_width, img_watermarked_height))

# Paste watermarked image onto result image
img_result.paste(img_watermarked, (0, 0))

# Paste logo image onto result image
img_result.paste(img_logo, (100, 100))

# Lighten logo image
enhancer = ImageEnhance.Brightness(img_logo)
img_logo_lightened = enhancer.enhance(1.5)

# Resize logo image
logo_new_size = (int(img_logo_width/2), int(img_logo_height/2))
img_logo_resized = img_logo_lightened.resize(logo_new_size)

# Paste the lightened and resized logo onto the result image
img_result.paste(img_logo_resized, (150, 150))

# Save result image
img_result.save("result_9.png")
