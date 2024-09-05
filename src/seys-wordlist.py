from PIL import Image, ImageDraw

# Define the image size and background color
width = 800
height = 1200
pixel_per_mm = 4 #3.7795275591
background_color = (255, 255, 255)  # White
major_lines = int(height / (pixel_per_mm * 2 * 4))
major_color = (100, 0, 150)
minor_color = (180, 180, 255)

# Create a new image with the specified size and background color
image = Image.new("RGB", (width, height), background_color)

# Create a draw object
draw = ImageDraw.Draw(image)

# Define the line color
line_color = (0, 0, 255)  # Blue

# Draw horizontal lines
#spacing of 2 mm
line_spacing = pixel_per_mm * 2
y = 1
for i in range(0, major_lines):

    draw.line([(0, y), (width, y)], fill=major_color)

    y += line_spacing

    for j in range(0, 3):
        draw.line([(0, y), (width, y)], fill=minor_color)
        y += line_spacing

draw.line([(0, y), (width, y)], fill=major_color)

# Save the image
#image.show()
image.save("seys-wordlist.png", dpi=(300, 300))