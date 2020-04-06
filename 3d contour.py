# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:25:50 2020

@author: vinnr
"""
import numpy as np

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
plt.style.use("seaborn-white")

def f(x,y):
    return np.sin(x) + np.cos(10 + y*x)*np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x,y)

Z = f(X, Y)


plt.contourf(X, Y, Z, 20, cmap ='RdGy')