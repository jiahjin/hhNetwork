# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 01:52:54 2023

@author: 12018
"""
import numpy as np
import sympy as sy
import ocrate as o
from Inputs import *
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Define symbols for voltage variables

VS = sy.symbols('VS0:%d' % numc)

for klok in range (int(klokmax)):
    t=(klok+1)*dt;

    m=snew(m,o.alpham(v),o.betam(v),dt) #update m
    h=snew(h,o.alphah(v),o.betah(v),dt) #update h
    n=snew(n,o.alphan(v),o.betan(v),dt) #update n
    gNa = gNabar*(m**3)*h   #sodium conductance
    gK = gKbar*(n**4)   #potassium conductance
    g = gNa+gK+gLbar    #total conductance
    gE=gNa*ENa+gK*EK+gLbar*EL;
    # x = sy.symbols('x')
    # rj = rnew(r,np.array([-50, -50, -50]))
    
    VS = np.array([0 for _ in range(numc)]).astype(float)
    def equations(VS):
        eqn = []
        rj = rnew(r,VS)
        for i in range (numc):
            Isyn = gcbar*(Vsyn-VS[i])*sum(a[i, :]*rj)
            eqn.append(VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t,t1p[i])+Isyn))/(1+(dt/C)*g[i]))
        return np.array(eqn)
    sol = fsolve(equations, VS)
    v = np.array(sol)    
    
    t_plot.append(t)
    for i in range(numc):
        v_plot[klok][i]=v[i]
   
    r = rnew(r,v)
# print(v_plot)    
plt.figure()
plt.plot(t_plot, v_plot)
# plt.plot(v_plot[:,1], v_plot[:,2])
# plt.legend()
# plt.xlabel('time(ms)')
# plt.ylabel('Voltage(V)')
# plt.show()

    
    
