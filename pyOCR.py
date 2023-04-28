# import pytesseract
# import numpy as np
# from PIL import Image

# filename = 'ads.jpeg'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)

# print(str(text).split('\n'))
# f = open("lang.txt", "w", encoding="utf-8")
# f.write(str(text))


# import cv2
# import numpy as np
# from PIL import Image

# method = cv2.TM_SQDIFF_NORMED
# small_image = cv2.imread('ad.jpg')
# large_image = cv2.imread('1st.png')
# w, h = large_image.shape[:-1]

# res = cv2.matchTemplate(small_image, large_image, method)
# threshold = .8
# loc = np.where(res >= threshold)
# a, b = loc
# print(a, b)

# for pt in zip(*loc[::-1]):  # Switch columns and rows
#     cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
# cv2.imwrite('result.png', large_image)

# image = cv2.imread('image.jpeg')
# # cv2.imshow('luck.png', image)
# # cv2.waitKey(0)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# template = cv2.imread('icon7.jpeg', 0)


# result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# threshold = .8
# print(np.where(result > threshold))

# height, width = template.shape[:2]

# top_left = max_loc
# bottom_right = (top_left[0] + width, top_left[1] + height)
# cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 5)

# cv2.imwrite('Rainforest.png', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

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
cityShortName = ["KNP", "LKO", "DEL", "PAT", "VNS",
                 "ALD", "GKP", "AGR", "MRD", "BHL", "MUZ"]
cityNameInStrip = ["Kanpur", "Lucknow", "Delhi", "Patna", "Varanasi",
                   "Allahabad", "Gorakhpur", "Agra", "Meerut", "Bhagalpur", "Muzaffarpur"]
date = "27-Apr-2023"
cityCodes = ["64", "11", "4", "84", "45",
             "79", "56", "193", "29", "205", "203"]

dictionary = {'Apr': '04'}

# editions loop
for i in range(9, len(cities)-1):
    counter = 0
    city = cities[i]
    cityCode = cityCodes[i]
    pageResponse = requests.get(
        "https://epaper.jagran.com/epaper/edition-today-" + cityCode + "-" + city + ".html")
    soup = BeautifulSoup(pageResponse.text, "lxml")

    noOfPages = soup.select('.info')
    pages = int(str(noOfPages[0]).split('\n')[4].split(' ')[-1][0:2])

    # pages loop
    for page in range(1, 2):
        print("https://epaper.jagran.com/epaper/" + date + "-" + cityCode +
              "-" + city + "-edition-" + city + "-page-" + str(page) + ".html")
        response = requests.get(
            "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + str(page) + ".html")
        soup = BeautifulSoup(response.text, "lxml")

        # get Strip ids
        page = 6
        paperStrips = soup.select('area')
        paperStripsId = paperStrips[0].get('id')

        print(paperStripsId)
        print("https://epaperapi.jagran.com/epaperimages/" + date.replace('-', '').replace(date[3:6], dictionary[date[3:6]]) + "/" + cityNameInStrip[0] + "/" +
              str(int(date[0:2])-1) + (cityShortName[0]) + "-pg" + str(page) + "-0/d" + "5144" + ".jpg")

    # extract paper link
    # id = "#image" + str(page)
    # imageTag = soup.select(id)
    # link = str(imageTag[0].get('data-src'))
    # responseImg = requests.get(link)

    #     with open("imagepy.jpg", "wb") as f:
    #         f.write(responseImg.content)
    #     # text extraction
    #     filename = 'imagepy.jpg'
    #     img1 = np.array(Image.open(filename))
    #     text = pytesseract.image_to_string(img1, lang='eng').lower().strip()

    #     # print((text).strip().split(' '))
    #     array = re.findall(r'[0-9]{4}-[0-9]{3}-[0-9]{4}|[+][0-9]{2}-[0-9]{3}-[0-9]{7}|[+][9,1]{2}[\s][0-9]{4}-[0-9]{6}|[0-9]{10}|\bclassifieds\b',
    #                        text)

    #     if len(a) != 0 and len(b) != 0 or len(array) != 0:
    #         counter += 1
    #         with open("images/DB_" + city + "_" + date.replace(date[3:6], dictionary[date[3:6]]) + "_0" + str(counter) + "_hin.jpeg", "wb") as f:
    #             f.write(responseImg.content)
