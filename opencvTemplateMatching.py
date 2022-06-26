import numpy as np
import cv2
import csv

header = ['method', 'item', 'score']
f = open('compare.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)
# write the header
writer.writerow(header)
# # write multiple rows
# writer.writerows(data)

# items = ['empty', 'grass', 'bush', 'tree', 'Hut', 'House', 'Mansion',
#  'Castle', 'floating mansion', 'triple castle', 'Bear', 'Church', 'Cathedral',
#  'treasure chest', 'big treasure chest', 'bot', 'rock', 'big rock', 'empty',
#  'triple castle']
items = ['grass', 'bush', 'tree']

# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]
number = 1

for item in items:
    print(item)
    for method in methods:
        if (method == cv2.TM_CCOEFF_NORMED):
            print('TM_CCOEFF_NORMED')
            useMethod = 'TM_CCOEFF_NORMED'
        elif (method == cv2.TM_CCORR_NORMED):
            print('TM_CCORR_NORMED')
            useMethod = 'TM_CCORR_NORMED'
        elif (method == cv2.TM_SQDIFF_NORMED):
            print('TM_SQDIFF_NORMED')
            useMethod = 'TM_SQDIFF_NORMED'
        for number in range(1,14):
            img1 = cv2.imread('./item/' + item + '/' + item + '00.jpg',0)
            img2 = cv2.imread('./item/' + item + '/' + item + f"{number:02d}" + '.jpg',0)
            result = cv2.matchTemplate(img1, img2, method)
            print(result)
            data = [useMethod, item, float(result)]
            writer.writerow(data)

f.close()
# print(type(result[0][0]))
