from PIL import Image, ImageDraw, ImageFont
import os

# Define the image size and background color
width = 800
height = 1200
pixel_per_mm = 4 #3.7795275591
background_color = (255, 255, 255)  # White
major_lines = int(height / (pixel_per_mm * 2 * 4))
major_color = (100, 0, 150)
minor_color = (180, 180, 255)
left_border_color = (255, 100, 100)
left_border = 30 * pixel_per_mm
row_width = pixel_per_mm * 8
font_name = "Ready For Fall.ttf"
font_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fonts", font_name)


#returns a font object that fits the given height
def get_font_sized(max_height):
    font_size = 1
    text = "A"
    step = 0.5
    font = ImageFont.truetype(font_path, font_size)

    while True :
        b = font.getbbox(text)
        print(b)

        if b[1] > max_height:
            break

        font_size += step
        font = ImageFont.truetype(font_path, font_size)

    return ImageFont.truetype(font_path, font_size - step)

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


# Draw vertical lines
max_col = (width - left_border) // row_width
x = left_border
for i in range(0, max_col + 1):
    draw.line([(x, 0), (x, height)], fill=minor_color)
    x += row_width

# Draw left border in red
x = left_border
draw.line([(x, 0), (x, height)], fill=left_border_color)


# Draw the text
# gets the font to draw a capital letter that fits the height of 3 sublines = 6 mm
font = get_font_sized( 2 * 3)
draw.text((left_border + 5, major_lines + pixel_per_mm*2), "SEYS ceci est un exemple", fill=(0, 0, 0), font=font, align="ls")

# Save the image
image.show()
image.save("seys-wordlist.png", dpi=(300, 300))