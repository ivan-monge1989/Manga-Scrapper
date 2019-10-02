from fpdf import FPDF
import fpdf
import os
from PIL import Image

image_list = [str(i + 1) + ".jpg" for i in range(179)]

pdf = FPDF('P', "in", (5, 7.5))

for image in image_list:
    cover = Image.open(image)
    width, height = cover.size
    width, height = float(width * 0.264583 / 25.4), float(height * 0.264583 / 25.4)

    if image == "5.jpg":
        pdf.add_page('L')
        pdf.image(image, 0, 0, 7.5, 5)
    else:
        pdf.add_page('P')
        pdf.image(image, 0, 0, 5, 7.5)




pdf.output("test1.pdf", "F")