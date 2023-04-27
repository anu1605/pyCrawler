from bs4 import BeautifulSoup
import requests
import time

import cv2
import numpy as np
from PIL import Image


date = "27-Apr-2023"
cityCode = "64"
city = "delhi-city"
pageResponse = requests.get(
    "https://epaper.jagran.com/epaper/edition-today-" + cityCode + "-" + city + ".html")
soup = BeautifulSoup(pageResponse.text, "lxml")


noOfPages = soup.select('.info')
pages = int(str(noOfPages[0]).split('\n')[4].split(' ')[-1][0:2])

for page in pages:
response = requests.get(
    "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + page + ".html")
soup = BeautifulSoup(response.text, "lxml")

# extract paper link
id = "#image" + page
imageTag = soup.select(id)
link = str(imageTag[0].get('data-src'))
responseImg = requests.get(link)


with open("imagepy.jpg", "wb") as f:
    f.write(responseImg.content)


method = cv2.TM_SQDIFF_NORMED
small_image = cv2.imread('icon3.jpeg')
large_image = cv2.imread('imagepy.jpg')
w, h = large_image.shape[:-1]

res = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
a, b = loc
if len(a) != 0 and len(b) != 0:
    with open("images/imagepy.jpg", "wb") as f:
        f.write(responseImg.content)

# for pt in zip(*loc[::-1]):  # Switch columns and rows
#     cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
# cv2.imwrite('result.png', large_image)


# write to text file
# f = open("imageLink.txt", "w")
# link = str(imageTag[0].get('data-src'))
# f.write(link)
