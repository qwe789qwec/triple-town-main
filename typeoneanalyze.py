import numpy as np
import cv2
import csv
import os
import pandas as pd
import plotly.express as px
import scipy
from scipy import stats
from scipy.stats import shapiro

items = ['empty', 'grass', 'bush', 'tree', 'hut', 'house',
 'ninjaBear', 'bear', 'church', 'cathedral', 'rock']
methods = ['TM_CCOEFF_NORMED', 'TM_CCORR_NORMED', 'TM_SQDIFF_NORMED']
header = ['method', 'item', 'compareItem', 'score', 'trueScore', 'compareResult']

data = pd.read_csv('./compareTypeOne.csv')

# fig = px.scatter(data, y='item', x='trueScore', color='method')
# fig.update_traces(marker_size=15)
# fig.update_layout(
#     title="correct compare",
#     xaxis_title="score",
#     yaxis_title="items",
#     legend_title="method",
#     font=dict(
#         # family="Courier New, monospace",
#         size=32,
#         # color="RebeccaPurple"
#     )
# )
# fig.show()

CCOEFF = data.loc[(data['method'] == 'TM_CCOEFF_NORMED')]
# print(CCOEFF)
passCCOEFF = CCOEFF.loc[(CCOEFF['compareResult'] == 'pass')]
falseCCOEFF = CCOEFF.loc[(CCOEFF['compareResult'] == 'false')]
passNumber = len(passCCOEFF)
falseNumber =len(falseCCOEFF)
print('CCOEFF: '+ 'pass:' + str(passNumber) + 'false:' + str(falseNumber))
print(passNumber/(passNumber + falseNumber))

CCORR = data.loc[(data['method'] == 'TM_CCORR_NORMED')]
# print(CCORR)
passCCOEFF = CCORR.loc[(CCORR['compareResult'] == 'pass')]
falseCCOEFF = CCORR.loc[(CCORR['compareResult'] == 'false')]
passNumber = len(passCCOEFF)
falseNumber =len(falseCCOEFF)
print('CCORR: '+ 'pass:' + str(passNumber) + 'false:' + str(falseNumber))
print(passNumber/(passNumber + falseNumber))

SQDIFF = data.loc[(data['method'] == 'TM_SQDIFF_NORMED')]
# print(SQDIFF)
passCCOEFF = SQDIFF.loc[(SQDIFF['compareResult'] == 'pass')]
falseCCOEFF = SQDIFF.loc[(SQDIFF['compareResult'] == 'false')]
passNumber = len(passCCOEFF)
falseNumber =len(falseCCOEFF)
print('SQDIFF: '+ 'pass:' + str(passNumber) + 'false:' + str(falseNumber))
print(passNumber/(passNumber + falseNumber))

