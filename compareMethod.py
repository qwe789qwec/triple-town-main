import numpy as np
import cv2
import csv
import os
import pandas as pd
import plotly.express as px
import scipy
from scipy import stats
from scipy.stats import shapiro

def showResult(way, torf, dframe):
    dataHandle = dframe.loc[data['method'] == way]
    print(torf + 'compare ' + way)
    meanValue = dataHandle.mean(axis='index')
    print('mean:' + str(meanValue['score']))
    stdValue = dataHandle.std(axis='index')
    print('std:' + str(stdValue['score']))
    ShapiroWilkTest = scipy.stats.shapiro(dataHandle['score'])
    print('Shapiro-Wilk Test = ' + str(ShapiroWilkTest))

def tTest(dframe1, dframe2, way1, way2):
    comp1 = dframe1.loc[data['method'] == way1]
    comp2 = dframe2.loc[data['method'] == way2]
    print(way1 + ' compare to ' + way2)
    print(scipy.stats.ttest_ind(comp1['score'], comp2['score']))

def shapiroWilk(dframe, way):
    comp = dframe.loc[data['method'] == way]
    print(shapiro(comp['score']))

methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

# items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house', 'mansion',
#  'castle', 'floatingMansion', 'tripleCastle', 'ninjaBear', 'bear', 'Church',
#  'Cathedral', 'treasure', 'bigTreasure', 'bot', 'rock', 'bigRock', 'tripleCastle']

items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house', 'mansion',
 'ninjaBear', 'bear', 'Church', 'Cathedral']

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

data = pd.read_csv('./compare.csv')
showResult('TM_CCOEFF_NORMED', 'success ',data)
showResult('TM_CCORR_NORMED', 'success ',data)
showResult('TM_SQDIFF_NORMED', 'success ',data)
# print(data)
fig = px.scatter(data, y='item1', x='score', color='method')
fig.update_traces(marker_size=15)
fig.update_layout(
    title="correct compare",
    xaxis_title="score",
    yaxis_title="items",
    legend_title="method",
    font=dict(
        # family="Courier New, monospace",
        size=32,
        # color="RebeccaPurple"
    )
)
fig.show()

print('')
wrongData = pd.read_csv('./failCompare.csv')
showResult('TM_CCOEFF_NORMED', 'fail ',wrongData)
showResult('TM_CCORR_NORMED', 'fail ',wrongData)
showResult('TM_SQDIFF_NORMED', 'fail ',wrongData)
fig = px.scatter(wrongData, y='item1', x='score', color='method')
fig.update_traces(marker_size=15)
fig.update_layout(
    title="worng compare",
    xaxis_title="score",
    yaxis_title="items",
    legend_title="method",
    font=dict(
        # family="Courier New, monospace",
        size=32,
        # color="RebeccaPurple"
    )
)
fig.show()

print('diff data')
tTest(data, wrongData, 'TM_CCOEFF_NORMED', 'TM_CCOEFF_NORMED')
tTest(data, wrongData, 'TM_CCORR_NORMED', 'TM_CCORR_NORMED')
tTest(data, wrongData, 'TM_SQDIFF_NORMED', 'TM_SQDIFF_NORMED')
print('')
print('data diff method')
tTest(data, data, 'TM_CCOEFF_NORMED', 'TM_CCORR_NORMED')
tTest(data, data, 'TM_CCOEFF_NORMED', 'TM_SQDIFF_NORMED')
tTest(data, data, 'TM_CCORR_NORMED', 'TM_SQDIFF_NORMED')
print('')
print('wrongData diff method')
tTest(wrongData, wrongData, 'TM_CCOEFF_NORMED', 'TM_CCORR_NORMED')
tTest(wrongData, wrongData, 'TM_CCOEFF_NORMED', 'TM_SQDIFF_NORMED')
tTest(wrongData, wrongData, 'TM_CCORR_NORMED', 'TM_SQDIFF_NORMED')
print('')
shapiroWilk(data, 'TM_CCOEFF_NORMED')
shapiroWilk(data, 'TM_SQDIFF_NORMED')
shapiroWilk(data, 'TM_CCORR_NORMED')
print('')
shapiroWilk(wrongData, 'TM_CCOEFF_NORMED')
shapiroWilk(wrongData, 'TM_SQDIFF_NORMED')
shapiroWilk(wrongData, 'TM_CCORR_NORMED')
