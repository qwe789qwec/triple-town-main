import numpy as np
import cv2

img1 = cv2.imread('./temp/dice51.jpg',0)
img2 = cv2.imread('./temp/dice44.jpg',0)

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

for method in methods:
    imgcompare = img1.copy()
    result = cv2.matchTemplate(imgcompare, img2, method)
    print(result)

print(type(result[0][0]))
