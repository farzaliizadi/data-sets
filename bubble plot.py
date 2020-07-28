# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 01:36:37 2020

@author: Izadi
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r'D:\desktop')
Data=pd.read_csv("BCG Matrix Data.csv")
Data.shape
Data.head()
# create data
x = Data['Value Share of Total F&N']
y = Data['Value Growth % YA']
z = Data.Value
value = pd.Series(Data['Items'])
colors = np.random.rand(10) 
# use the scatter function
i = [0, 25]
j = [5, 5]
k= [12.5,12.5]
m =[-15,25]
plt.plot(i,j, color= 'black')
plt.plot(k,m, color= 'black')
plt.title("BCG Matrix")
plt.scatter(x, y, s=z/10000, c=colors, label=value)
plt.xlabel("Shares")
plt.ylabel("Growth")
plt.legend(loc=6)
plt.show()
