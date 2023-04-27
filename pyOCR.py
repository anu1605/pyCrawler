# import pytesseract
# import numpy as np
# from PIL import Image

# filename = 'images/1st.png'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1, lang="hin")

# print(text)
# f = open("lang.txt", "w", encoding="utf-8")
# f.write(str(text))


# import cv2
# import numpy as np
# from PIL import Image

# method = cv2.TM_SQDIFF_NORMED
# small_image = cv2.imread('icon3.jpeg')
# large_image = cv2.imread('1st.png')
# w, h = large_image.shape[:-1]

# res = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
# threshold = .8
# loc = np.where(res >= threshold)
# a, b = loc

# for pt in zip(*loc[::-1]):  # Switch columns and rows
#     cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
# cv2.imwrite('result.png', large_image)


from bs4 import BeautifulSoup
import requests

date = "25-Apr-2023"
cityCode = "64"
city = "kanpur"
page = "12"
