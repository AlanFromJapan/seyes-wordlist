from PIL import Image, ImageDraw, ImageFont
import os

# Define the image size and background color
width = 800
height = int(width * 1.4142)  # A4 paper aspect ratio
pixel_per_mm = 4 #3.7795275591
background_color = (255, 255, 255)  # White
major_line_height = int(height / (pixel_per_mm * 2 * 4))
major_line_offset = 1
major_color = (100, 0, 150)
minor_color = (180, 180, 255)
left_border_color = (255, 100, 100)
left_border = 30 * pixel_per_mm
row_width = pixel_per_mm * 8
font_name = "SimpleRonde-Regular.ttf"
font_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "fonts", font_name)


#returns a font object that fits the given height
def get_font_sized(max_height):
    font_size = 1
    text = "A"
    step = 0.5
    font = ImageFont.truetype(font_path, font_size)

    while True :
        b = font.getbbox(text, anchor="ls")
        # box is (left, top, right, bottom), if anchor is "ls" (= left baseline) then it's the height of a capital "A"
        if abs(b[1]) > max_height:
            break

        font_size += step
        font = ImageFont.truetype(font_path, font_size)

    return ImageFont.truetype(font_path, font_size - step)


# draws text on the image, line by line
def draw_text(draw, text, x, y, font):
    #the font is slightly too big, so we reduce the y position. Might be the provision for accented characters that getbox() accounts for. Why by THIS amount? I don't know.
    y -= pixel_per_mm //2
    for t in text:
        draw.text((x, y), t, fill=(0,0,0), font=font, anchor="ls")
        y += pixel_per_mm * 2 * 4



# Create a new image with the specified size and background color
image = Image.new("RGB", (width, height), background_color)

# Create a draw object
draw = ImageDraw.Draw(image)

# Define the line color
line_color = (0, 0, 255)  # Blue

# Draw horizontal lines
#spacing of 2 mm
line_spacing = pixel_per_mm * 2
y = major_line_offset
for i in range(0, major_line_height):

    draw.line([(0, y), (width, y)], fill=major_color)

    y += line_spacing

    for j in range(0, 3):
        draw.line([(0, y), (width, y)], fill=minor_color)
        y += line_spacing
#final major line
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
font = get_font_sized(pixel_per_mm * 2 * 3)
y = major_line_height + major_line_offset
x = left_border + 5

draw_text(draw, ["il y a", "un jardin", "quatre", "du chocolat"], x, y, font)

# Save the image
image.show()
image.save("seys-wordlist.png", dpi=(300, 300))