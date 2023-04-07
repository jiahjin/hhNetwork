# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:56:47 2023

@author: 12018
"""
import numpy as np
import sympy as sy


def alpham(v):

    theta = (v + 35) / 10
    a = np.zeros_like(v, dtype=float)
    mask = (theta != 0)
    a[mask] = 1.0 * theta[mask] / (1 - np.exp(-theta[mask]))
    a[~mask] = 1.0

    return a
    # theta = (v + 45) / 10
    # a = np.zeros_like(v, dtype=float)
    # mask = (theta != 0)
    # a[mask] = 1.0 * theta[mask] / (1 - np.exp(-theta[mask]))
    # a[~mask] = 1.0
    # return a


def betam(v):
    theta = (v+60)/18
    b = 4*np.exp(theta)
    return b
    # theta = (v+70)/18
    # b = 4.0*np.exp(-theta)
    # return b

def alphah(v):
    theta = (v+60)/20;
    a=0.07*np.exp(theta)
    return a
    # theta = (v+70)/20;
    # a=0.07*np.exp(-theta)
    # return a


def betah(v):
    theta = (v+30)/10
    b=1.0/(1+np.exp(-theta));
    return b


def alphan(v):
    theta = (v + 50)
    a = np.zeros_like(v, dtype=float)
    mask = (theta != 0)
    a[mask] = 0.01 * theta[mask] / (1 - np.exp(-0.1*theta[mask]))
    a[~mask] = 0.1
    
    # theta=(v+60)/10
    # a = np.zeros_like(v, dtype=float)
    # mask = (theta != 0)
    # a[mask] = 0.1 * theta[mask] / (1 - np.exp(-theta[mask]))
    # a[~mask] = 0.1
    return a

def betan(v):
    theta = (v+60)/80
    b = 0.125*np.exp(theta)
    # theta = (v+70)/80;
    # b=0.125*np.exp(-theta); 
    return b


# VS = [sy.Symbol('k')]*numc
# print(VS)

# VS = sy.IndexedBase('VS',numc)

# var = []
# for i in range(numc):
#     var.append(VS[i])
    

# f1 = VS[0]-2*VS[1]
# f2 = VS[0]+VS[1]-3

# system = [f1, f2]
# jj= sy.solve(system, var)
# print(jj)

