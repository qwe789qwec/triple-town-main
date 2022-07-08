import numpy as np
import cv2
import csv
import os

csvName = 'compareTypeOne.csv'

header = ['method', 'item', 'compareItem', 'score', 'trueScore', 'compareResult']
f = open(csvName, 'w', encoding='UTF8', newline='')
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

for method in methods:
    number = 2
    for compare in items:
        comparePath = './item/' + compare + '/' + compare + str(number) + '.jpg'
        compare_exists = os.path.exists(comparePath)

        while compare_exists:
            if method != cv2.TM_SQDIFF_NORMED:
                lastResult = 0
            else:
                lastResult = 100
            trueScore = 0

            for tamplate in items:
                tamplatePath = './item/' + tamplate + '/' + tamplate + '1.jpg'
                tamplateImg = cv2.imread(tamplatePath,0)
                compareImg = cv2.imread(comparePath,0)
                result = cv2.matchTemplate(tamplateImg, compareImg, method)

                if method != cv2.TM_SQDIFF_NORMED:
                    if lastResult < result:
                        lastResult = result
                        identifyItem = tamplate
                else:
                    if lastResult > result:
                        lastResult = result
                        identifyItem = tamplate

                if compare == tamplate:
                        trueScore = result
            if (method == cv2.TM_CCOEFF_NORMED):
                useMethod = 'TM_CCOEFF_NORMED'
                lastResult = (1 + lastResult)/2
                trueScore = (1 + trueScore)/2
            elif (method == cv2.TM_CCORR_NORMED):
                useMethod = 'TM_CCORR_NORMED'
            elif (method == cv2.TM_SQDIFF_NORMED):
                useMethod = 'TM_SQDIFF_NORMED'
                lastResult = 1 - lastResult
                trueScore = 1 - trueScore
            else:
                useMethod = 'error'
                lastResult = 999999
                trueScore = 999999

            if(compare == identifyItem):
                compareResult = 'pass'
            else:
                compareResult = 'false'


            data = [useMethod, compare, identifyItem, float(lastResult*100), float(trueScore*100), compareResult]
            writer.writerow(data)
            number = number + 1
            comparePath = './item/' + compare + '/' + compare + str(number) + '.jpg'
            compare_exists = os.path.exists(comparePath)

        number = 2

f.close()
# print(type(result[0][0]))
