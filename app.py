from bs4 import BeautifulSoup
import requests
import time
import pytesseract
import re

import cv2
import numpy as np
from PIL import Image
from datetime import datetime
import os

cities = ["kanpur", "Lucknow", "delhi-city", "Patna-Nagar", "varanasi-city",
          "Prayagraj-City", "Gorakhpur-City", "Agra", "Meerut", "bhagalpur", "muzaffarpur-nagar"]
date = "29-Apr-2023"
cityCodes = ["64", "11", "4", "84", "45",
             "79", "56", "193", "29", "205", "203"]

dictionary = {'Apr': '04'}
# cityDictionary = {"delhi-city" : "Delhi" ,"Patna-Nagar" : "Patna" , varanasi-city }


for i in range(1, len(cities)):
    counter = 0
    city = cities[i]
    cityCode = cityCodes[i]
    pageResponse = requests.get(
        "https://epaper.jagran.com/epaper/" + date + "-" + cityCode + "-" + city + "-edition-" + city + "-page-" + "1" + ".html")
    soup = BeautifulSoup(pageResponse.text, "lxml")

    # noOfPages = soup.select('.info')
    # pages = int(str(noOfPages[0]).split('\n')[4].split(' ')[-1][0:2])

    noOfPages = soup.select("#totalpageno")[0].get("value")

    for page in range(1, int(noOfPages)):
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
        imagePaths = ["cities/" + city + ".jpeg", "icon.jpg"]

        method = cv2.TM_SQDIFF_NORMED
        large_imageS = cv2.imread('imagepy.jpg',  cv2.IMREAD_UNCHANGED)
        for size in [100, 200, 300, 400]:
            # print(size)
            up_width = large_imageS.shape[0] + size
            up_height = large_imageS.shape[1] + size

            up_points = (up_width, up_height)
            large_image = cv2.resize(
                large_imageS, up_points, interpolation=cv2.INTER_LINEAR)

            # text extraction
            filename = 'imagepy.jpg'
            img1 = np.array(large_image)

            text = pytesseract.image_to_string(img1, lang="eng").lower()
            # print(text)

            array = re.findall(r'[0-9]{4}-[0-9]{3}-[0-9]{4}|[+][0-9]{2}-[0-9]{3}-[0-9]{7}|[+][9,1]{2}[\s][0-9]{4}-[0-9]{6}|[0-9]{10}',
                               text)

            if len(array) != 0:
                counter += 1
                number = "_"
                dateObj = datetime.strptime(date.replace(
                    date[3:6], dictionary[date[3:6]]), '%d-%m-%Y')
                formateDate = dateObj.strftime("%Y-%m-%d")
                formatCity = city.lower().replace("-city", "").replace("-nagar", "").capitalize()

                with open("images/DJ_" + formatCity + "_" + formateDate + number + str(counter) + "_hin.jpeg", "wb") as f:
                    f.write(responseImg.content)
                break
