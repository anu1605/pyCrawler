# import pytesseract
# import numpy as np
# from PIL import Image

# filename = 'ads.jpeg'
# img1 = np.array(Image.open(filename))
# text = pytesseract.image_to_string(img1)

# print(str(text).split('\n'))
# f = open("lang.txt", "w", encoding="utf-8")
# f.write(str(text))


import cv2
import numpy as np
from PIL import Image

method = cv2.TM_SQDIFF_NORMED
small_image = cv2.imread('ad.jpg')
large_image = cv2.imread('1st.png')
w, h = large_image.shape[:-1]

res = cv2.matchTemplate(small_image, large_image, method)
threshold = .8
loc = np.where(res >= threshold)
a, b = loc
print(a, b)

for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
cv2.imwrite('result.png', large_image)

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
