# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:11:16 2020

@author: Izadi
"""
import os
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(r'D:\desktop\Python_DM_ML_BA\anscombe 4 datasets')
df = pd.read_csv('anscombe.csv')
df.shape
df.head()


f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.regplot(df.x, df.y, fit_reg=True, scatter_kws={"s": 100}, ax=axes[0, 0])
sns.regplot(df.z, df.w, fit_reg=True, scatter_kws={"s": 100}, ax=axes[0, 1])
sns.regplot(df.u, df.v, fit_reg=True, scatter_kws={"s": 100}, ax=axes[1, 0])
sns.regplot(df.s, df.t, fit_reg=True, scatter_kws={"s": 100}, ax=axes[1, 1])
plt.show()
