# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 01:52:54 2023

@author: 12018
"""
import numpy as np
import sympy as sp
from ocrate import *
from Inputs import *


for klok in range (int(klokmax)):
    t=(klok+1)*dt;
    for i in range(numc):
        m=snew(m,alpham(v[i]),betam(v[i]),dt) #update m
        h=snew(h,alphah(v[i]),betah(v[i]),dt) #update h
        n=snew(n,alphan(v[i]),betan(v[i]),dt) #update n
        gNa = gNabar*(m**3)*h   #sodium conductance
        gK = gKbar*(n**4)   #potassium conductance
        g = gNa+gK+gLbar    #total conductance
        gE=gNa*ENa+gK*EK+gLbar*EL; #gE=g•E
        v_old = v;
        
        #symbol
        VS = sy.IndexedBase('VS',numc)
        var = []
        var.append(VS[i])
        
        #equations
        eqn =[]
        rj = rnew(r,VS)
        eqn[i] = VS[i]==(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i]);
            
            

        f1 = VS[0]-2*VS[1]
        f2 = VS[0]+VS[1]-3

        system = [f1, f2]
        jj= sy.solve(system, var)
        print(jj)
        vs = sp.symbol('k', integer=True)
        VS = [vs]*numc

        VS = sp.symbols('VS',[1,numc]); #Symbol for V
        # update v:
        for i in range(numc):
            rj = rnew(r,VS)
            ar = a #aij*rj(t)*(Vsyn-Vi)
            sumarv = 
%update v:
for i = 1: numc
    rj = rnew(r,VS);
    arv = a(i, :).*rj.*(20-VS);
    sumarv = sum(arv(i));
    Isyn = gcbar*sumarv;
    eqn(i) = VS(i)==(v(i)+(dt/C)*(gE(i)+izero(t)+Isyn))/(1+(dt/C)*g(i));
end
        
y, z = symbols('y, z', real = True) # y = angle between r_cb and x-axis, z = output angle
i = symbol('i', integer=True)
            