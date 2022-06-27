import numpy as np
import cv2
import csv
import os

header = ['method', 'item', 'score']
f = open('compare.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)
# write the header
writer.writerow(header)
# # write multiple rows
# writer.writerows(data)

items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house', 'mansion',
 'castle', 'floatingMansion', 'tripleCastle', 'ninjaBear', 'bear', 'Church',
 'Cathedral', 'treasure', 'bigTreasure', 'bot', 'rock', 'bigRock', 'tripleCastle']

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
number = 1

for item in items:
    # print(item)
    for method in methods:
        if (method == cv2.TM_CCOEFF_NORMED):
            # print('TM_CCOEFF_NORMED')
            useMethod = 'TM_CCOEFF_NORMED'
        elif (method == cv2.TM_CCORR_NORMED):
            # print('TM_CCORR_NORMED')
            useMethod = 'TM_CCORR_NORMED'
        elif (method == cv2.TM_SQDIFF_NORMED):
            # print('TM_SQDIFF_NORMED')
            useMethod = 'TM_SQDIFF_NORMED'
        number = 2
        # img2Name = './item/' + item + '/' + item + f"{number:02d}" + '.jpg'
        img2Name = './item/' + item + '/' + item + str(number) + '.jpg'
        file_exists = os.path.exists(img2Name)
        while file_exists:
            img1 = cv2.imread('./item/' + item + '/' + item + '1.jpg',0)
            img2 = cv2.imread(img2Name,0)
            result = cv2.matchTemplate(img1, img2, method)
            h, w = img2.shape
            if h == 65:
                # print(result)
                data = [useMethod, item, float(result*100)]
                writer.writerow(data)
            else:
                print(img2Name)
            number = number + 1
            img2Name = './item/' + item + '/' + item + str(number) + '.jpg'
            file_exists = os.path.exists(img2Name)

f.close()
# print(type(result[0][0]))
