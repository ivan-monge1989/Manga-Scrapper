#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests
import re
from fpdf import FPDF
from PIL import Image


# HTML link to save images from
html_link = "https://manganelo.com/chapter/ranma_12/chapter_1"

# Select where to save images
# root = Tk()
# root.withdraw()
# savedir = filedialog.askdirectory(initialdir="/Users/ivancito", title="Select folder to save images")
#

# Request website and parse it
r = requests.get(html_link)
soup = BeautifulSoup(r.content, "lxml")

# Loop through all images in the HTML
# TODO: Convert this into a function
img_links = []
for image in soup.find_all('img'):
    #Find the /##.jpg pattern and append to the list
    pattern = r"/\d+\.jpg"
    if re.search(pattern, image.get('src')):
        img_links.append(image.get('src'))


# Create fileName list
# TODO: Convert this into a function
fileNames = []
for ii in range(len(img_links)):
    fileNames.append(re.findall(r"\d+.jpg", img_links[ii])[0])


# Request images from website and save them
for ii in range(len(img_links)):
    image_request = requests.get(img_links[ii])
    print(img_links[ii])
    with open(fileNames[ii], 'wb') as f:
        f.write(image_request.content)


# # Convert Images to pdf
# pdf = FPDF()
#
# for image in fileNames[0:9]:
#     pdf.add_page()
#     pdf.image(image, x=0, y=0)
#
# pdf.output("yourfile.pdf", "F")