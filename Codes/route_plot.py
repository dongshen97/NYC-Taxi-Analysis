# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:57:09 2020

@author: Songyu Yan
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib



dfs = []


df = pd.read_csv('testing.csv', usecols=[6,7,8,9])

p1 = df['Pickup_longitude']
p2 = df['Pickup_latitude']
fig, ax = plt.subplots()
ax.xlim = (-74.06,-73.77)
ax.ylim = (40.61, 40.91)
ax.scatter(p1, p2,color = 'black',s=1.0,alpha = .5)

fig.savefig('./routes.png')
