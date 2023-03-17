# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:56:47 2023

@author: 12018
"""
import numpy as np
import sympy as sy
numc= 2

def alpham(v):
    theta = (v+45)/10
    if theta ==0:
        a = 1.0
    else:
        a = 1.0*theta/(1-np.exp(-theta))
    return a
def betam(v):
    theta = (v+70)/18
    b = 4.0*np.exp(-theta)
    return b

def alphah(v):
    theta = (v+70)/20;
    a=0.07*np.exp(-theta)
    return a
def betah(v):
    theta = (v+40)/10
    b=1.0/(1+np.exp(-theta));
    return b

def alphan(v):
    theta=(v+60)/10
    if theta== 0:
        a = 0.1
    else:
        a=0.1*theta/(1-np.exp(-theta));
    return a
def betan(v):
    theta = (v+70)/80;
    b=0.125*np.exp(-theta); 
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

