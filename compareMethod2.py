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

data = pd.read_csv('./compareAll.csv')
data['YorN'] = (data['item1'] == data['item2'])
# data['mean'] = data.groupby(['YorN', 'method', 'item1'], as_index=False).mean()
# data.loc[(data['method'] == method) & (data['item1'] == item) & (data['YorN'] == True)]['score'].mean(axis='index')

for item in items:
    for method in methods:
        data.loc[(data['method'] == method) & (data['item1'] == item) & (data['YorN'] == True), 'mean'] = data.loc[(data['method'] == method) & (data['item1'] == item) & (data['YorN'] == True)]['score'].mean(axis='index')
        data.loc[(data['method'] == method) & (data['item1'] == item) & (data['YorN'] == False), 'mean'] = data.loc[(data['method'] == method) & (data['item1'] == item) & (data['YorN'] == False)]['score'].mean(axis='index')
# meanValue = dframe.loc[data['TM_CCOEFF_NORMED'] == way &&].mean(axis='index')
# meanValue = dframe.loc[data['TM_CCORR_NORMED'] == way && ].mean(axis='index')
# meanValue = dframe.loc[data['TM_SQDIFF_NORMED'] == way &&].mean(axis='index')

fig = px.scatter(data, y='item1', x='mean', color='method', symbol="YorN")
fig.update_traces(marker_size=15)
fig.update_layout(
    title="method compare",
    xaxis_title="score",
    yaxis_title="items",
    legend_title="method",
    font=dict(
        # family="Courier New, monospace",
        size=32,
        # color="RebeccaPurple"
    )
)
# fig.show()

fig = px.scatter(data.loc[(data['YorN'] == True)], y='item1', x='mean', color='method')
fig.update_traces(marker_size=15)
fig.update_layout(
    title="method compare",
    xaxis_title="score",
    yaxis_title="items",
    legend_title="method",
    font=dict(
        # family="Courier New, monospace",
        size=32,
        # color="RebeccaPurple"
    )
)
# fig.show()

fig = px.scatter(data.loc[(data['YorN'] == False)], y='item1', x='mean', color='method')
fig.update_traces(marker_size=15)
fig.update_layout(
    title="method compare",
    xaxis_title="score",
    yaxis_title="items",
    legend_title="method",
    font=dict(
        # family="Courier New, monospace",
        size=32,
        # color="RebeccaPurple"
    )
)
# fig.show()


for method in methods:
    set1 = data.loc[(data['method'] == method) & (data['YorN'] == True)]['mean']
    set2 = data.loc[(data['method'] == method) & (data['YorN'] == False)]['mean']
    print(method)
    print(scipy.stats.ttest_ind(set1, set2))
    print(shapiro(set1))
    print(shapiro(set2))
