# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:49:04 2017

@author: user11
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def Cp(mylist, usl, lsl):
    arr = np.array(mylist)
    arr = arr.ravel()
    sigma = np.std(arr)
    Cp = float((usl - lsl) / (6*sigma))
    return Cp


def Cpk(mylist, usl, lsl):
    arr = np.array(mylist)
    arr = arr.ravel()
    sigma = np.std(arr)
    m = np.mean(arr)

    Cpu = float(usl - m) / (3*sigma)
    Cpl = float(m - lsl) / (3*sigma)
    Cpk = np.min([Cpu, Cpl])
    return Cpk


def Histo(data):
    x = np.array(data)
    xmin = x.min()
    xmax = x.max()
    mu, std = stats.norm.fit(data)
    x_smooth = np.linspace(xmin, xmax, 200)
    kde = stats.gaussian_kde(x)
    y1 = kde(x_smooth)
    px_smooth = norm.pdf(x_smooth, mu, std)
    plt.hist(data,'auto', normed=True, alpha=0.6)
    plt.plot(x_smooth, px_smooth,'k', linewidth=2)
    plt.plot(x_smooth,y1)
    plt.show()

#for item in df[0].drop_duplicates():
#    df1 = df[df[0]==item]
#    Histo(df1[1].dropna())

#fig,axes = plt.subplots(nrows=6, ncols=5, sharex=True, sharey=True)
#for item, j in zip(df[0].drop_duplicates(),range(i)):
#    df1 = df[df[0]==item]
#    plt.subplot(6,5,j+1)
#    Histo(df1[1].dropna())

