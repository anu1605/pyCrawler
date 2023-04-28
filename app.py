from bs4 import BeautifulSoup
import requests
import time
import pytesseract
import re

import cv2
import numpy as np
from PIL import Image


cities = ["kanpur", "Lucknow", "delhi-city", "Patna-Nagar", "varanasi-city",
          "Prayagraj-City", "Gorakhpur-City", "Agra", "Meerut", "bhagalpur", "muzaffarpur-nagar"]
date = "28-Apr-2023"
cityCodes = ["64", "11", "4", "84", "45",
             "79", "56", "193", "29", "205", "203"]

dictionary = {'Apr': '04'}


for i in range(0, len(cities)):
    counter = 0
    city = cities[i]
    cityCode = cityCodes[i]
    pageResponse = requests.get(
        "https://epaper.jagran.com/epaper/edition-today-" + cityCode + "-" + city + ".html")
    soup = BeautifulSoup(pageResponse.text, "lxml")

    noOfPages = soup.select('.info')
    pages = int(str(noOfPages[0]).split('\n')[4].split(' ')[-1][0:2])

    for page in range(1, pages):
        print("https://epaper.jagran.com/epaper/" + date + "-" + cityCode +
              "-" + city + "-edition-" + city + "-page-" + str(page) + ".html")
        response = requests.get(
            "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + str(page) + ".html")
        soup = BeautifulSoup(response.text, "lxml")

    # extract paper link
        id = "#image" + str(page)
        imageTag = soup.select(id)
        link = str(imageTag[0].get('data-src'))
        responseImg = requests.get(link)

        with open("imagepy.jpg", "wb") as f:
            f.write(responseImg.content)

        # match image
        if city != "bhagalpur" and city != "muzaffarpur-nagar":
            method = cv2.TM_SQDIFF_NORMED
            imPath = "cities/" + city + ".jpeg"
            small_image = cv2.imread(imPath)
            large_image = cv2.imread('imagepy.jpg')
            w, h = large_image.shape[:-1]

            res = cv2.matchTemplate(
                small_image, large_image, cv2.TM_CCOEFF_NORMED)
            threshold = .8
            loc = np.where(res >= threshold)
            a, b = loc

        # text extraction
        filename = 'imagepy.jpg'
        img1 = np.array(Image.open(filename))
        text = pytesseract.image_to_string(img1, lang='eng').lower().strip()

        # print((text).strip().split(' '))
        array = re.findall(r'[0-9]{4}-[0-9]{3}-[0-9]{4}|[+][0-9]{2}-[0-9]{3}-[0-9]{7}|[+][9,1]{2}[\s][0-9]{4}-[0-9]{6}|[0-9]{10}|\bclassifieds\b',
                           text)

        if len(a) != 0 and len(b) != 0 or len(array) != 0:
            counter += 1
            with open("images/DB_" + city + "_" + date.replace(date[3:6], dictionary[date[3:6]]) + "_0" + str(counter) + "_hin.jpeg", "wb") as f:
                f.write(responseImg.content)

# for pt in zip(*loc[::-1]):  # Switch columns and rows
#     cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
# cv2.imwrite('result.png', large_image)


# write to text file
# f = open("imageLink.txt", "w")
# link = str(imageTag[0].get('data-src'))
# f.write(link)


# f = open("lang.txt", "w", encoding="utf-8")
# f.write(str(text))
