import numpy as np
import cv2
import csv
import os

header = ['method', 'item1', 'item2', 'score']
# f = open('failCompare.csv', 'w', encoding='UTF8', newline='')
f = open('compareAll.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)
# write the header
writer.writerow(header)
# # write multiple rows
# writer.writerows(data)

# items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house', 'mansion',
#  'castle', 'floatingMansion', 'tripleCastle', 'ninjaBear', 'bear', 'Church',
#  'Cathedral', 'treasure', 'bigTreasure', 'bot', 'rock', 'bigRock', 'tripleCastle']

items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house',
 'ninjaBear', 'bear', 'church', 'cathedral', 'rock']

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF, cv2.TM_CCORR, cv2.TM_SQDIFF]
lestItem = '0'

for item in items:
    # print(item)
    for method in methods:
        number = 2
        for comItem in items:
            img1Name = './item/' + item + '/' + item + '1.jpg'
            img2Name = './item/' + comItem + '/' + comItem + str(number) + '.jpg'
            img1_exists = os.path.exists(img1Name)
            img2_exists = os.path.exists(img2Name)
            while img1_exists and img2_exists:
                img1 = cv2.imread(img1Name,0)
                img2 = cv2.imread(img2Name,0)
                result = cv2.matchTemplate(img1, img2, method)
                if (method == cv2.TM_CCOEFF_NORMED):
                    useMethod = 'TM_CCOEFF_NORMED'
                    result = (1 + result)/2
                elif (method == cv2.TM_CCORR_NORMED):
                    useMethod = 'TM_CCORR_NORMED'
                elif (method == cv2.TM_SQDIFF_NORMED):
                    useMethod = 'TM_SQDIFF_NORMED'
                    result = 1 - result
                else:
                    useMethod = 'error'
                    result = 999999

                h, w = img2.shape
                if h == 65:
                    data = [useMethod, item, comItem, float(result*100)]
                    writer.writerow(data)
                else:
                    print(img2Name)
                number = number + 1
                img2Name = './item/' + comItem + '/' + comItem + str(number) + '.jpg'
                img2_exists = os.path.exists(img2Name)
            number = 2

f.close()
# print(type(result[0][0]))
