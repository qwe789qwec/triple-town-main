import numpy as np
import cv2

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
    for number in range(1,14):
        img1 = cv2.imread('./item/' + item + '/' + item + '00.jpg',0)
        img2 = cv2.imread('./item/' + item + '/' + item + f"{number:02d}" + '.jpg',0)
        h, w = img2.shape
        if(h == 65):
            for method in methods:
                imgcompare = img1.copy()
                result = cv2.matchTemplate(imgcompare, img2, method)
                if (method == cv2.TM_CCOEFF_NORMED):
                    print('TM_CCOEFF_NORMED')
                elif (method == cv2.TM_CCORR_NORMED):
                    print('TM_CCORR_NORMED')
                elif (method == cv2.TM_SQDIFF_NORMED):
                    print('TM_SQDIFF_NORMED')
                print(result)
        else:
            print(item + f"{number:02d}")

print(type(result[0][0]))
