import numpy as np
import cv2
import csv
import os
import pandas as pd
import plotly.express as px

methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house', 'mansion',
 'castle', 'floatingMansion', 'tripleCastle', 'ninjaBear', 'bear', 'Church',
 'Cathedral', 'treasure', 'bigTreasure', 'bot', 'rock', 'bigRock', 'tripleCastle']

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

data = pd.read_csv('./failCompare.csv')
# print(data)
fig = px.scatter(data, y='item1', x='score', color='method')
fig.show()
