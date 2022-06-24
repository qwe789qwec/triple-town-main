import cv2
import numpy as np
bush = cv2.imread('./item/grass.png')
bush1 = cv2.imread('./item/grass.png')
bushcut = cv2.imread('./item/grasscut.png')

hsv_bush = cv2.cvtColor(bush, cv2.COLOR_BGR2HSV)
hsv_bush1 = cv2.cvtColor(bush1, cv2.COLOR_BGR2HSV)
hsv_bushcut = cv2.cvtColor(bushcut, cv2.COLOR_BGR2HSV)

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0, 1]

hsv_bush = cv2.calcHist([hsv_bush], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hsv_bush, hsv_bush, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
hsv_bush1 = cv2.calcHist([hsv_bush1], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hsv_bush1, hsv_bush1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
hsv_bushcut = cv2.calcHist([hsv_bushcut], channels, None, histSize, ranges, accumulate=False)
cv2.normalize(hsv_bushcut, hsv_bushcut, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

compare_method = cv2.HISTCMP_CORREL

cv2.imshow('hsv_bush1',hsv_bush1)
cv2.imshow('hsv_bush',hsv_bush)
cv2.imshow('hsv_bushcut',hsv_bushcut)

bush1_bush1 = cv2.compareHist(hsv_bush1, hsv_bush1, compare_method)
bush1_bush = cv2.compareHist(hsv_bush1, hsv_bush, compare_method)
bush1_bushcut = cv2.compareHist(hsv_bush1, hsv_bushcut, compare_method)

print('bush1_bush1 Similarity = ', bush1_bush1)
print('bush1_bush Similarity = ', bush1_bush)
print('bush1_bushcut Similarity = ', bush1_bushcut)

cv2.waitKey(0)                                    # 按下任意鍵停止
