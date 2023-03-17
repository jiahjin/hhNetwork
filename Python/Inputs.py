# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:14:30 2023

@author: 12018
"""
import numpy as np
import sympy as sy
from ocrate import *

# nxnsynaptic adjacency matrix
a = np.array([[0, 1, 1],
              [1, 0, 1],
              [1, 1, 0]])
# numc = n
numc = len(a)

#initialize membrane parameters: 

#membrane capacitance per unit area:
C=1.0; #(muF/cm^2)
#max possible Na+ conductance per unit area:
gNabar=120; #((muA/mV)/cm~2) 1/R/A
#max possible K+ conductance per unit area:
gKbar=36; #((muA/mV)/cm~2)
#leakage conductance per unit area:
gLbar=0.3; #((muA/mV)/cm~2) 
#Na+ equilibrium potential: 
ENa = 45; #(mV)
#K+ equilibrium potential:
EK = -82; #(mV)
#leakage channel reversal potential:
EL = -59; #(mV)
#maximum specific conductance:
gcbar = 0.04;

#initialize time step and experiment duration:
dt=0.1; #time step duration (ms)
tmax=1; #duration of experiment (ms)
#total number of time steps in the experiment:
klokmax= np.ceil(tmax/dt); #round up to integer

#initialize arrays that hold data for plotting:
mhn_plot=[]
v_plot=[]
t_plot=[]

#initialize parameters that define the experiment:
#the neuron is at rest (v= -70 mV) prior to t=O;
#at t=O a current shock is applied after which v= -55 mV;
#voltage prior to t=O:
vhold= [-70 for _ in range(numc)]
#voltage just after t=O:
#vstart= -55; %(mV)
vstart= [-55 for _ in range(numc)]
#(change in v is result of current shock applied at t=O)

#simulate time prior to t=O: 

#set m,h,n equal to their steady values
#under constant-v conditions:
m =[0]*numc; h=[0]*numc; n =[0]*numc
for i in range(numc):
    v=vhold[i]
    m[i]=alpham(v)/(alpham(v)+betam(v))
    h[i]=alphah(v)/(alphah(v)+betah(v))
    n[i]=alphan(v)/(alphan(v)+betan(v))
    
# compute initial r
taur = 0.5;
taud = 8; 
V0 = 20;
ri = 1-1/taud/(1+np.exp(-v+V0));
r = [ri]*numc

#now let voltage jump to its value
#just after t=O, without making
#any further change in m,h,n:
v=vstart;

#then a subsequent 15 muA current pulse of 1 ms duration
#is applied beginning at t=lO ms.
t1p=10; #starting time (ms)
t2p=t1p+1; #stopping time (ms) 
ip=50;  #current applied (muA) 

#initialize checking parameter
check=1
#set check=l to enable self-checking
#set check=O to disable self-checking 

def snew(s_old, alpha, beta, dt):
    s=(s_old+dt*alpha)/(1+dt*(alpha+beta))
    # if(check):
    #     chsnew = (s-s_old)/dt -(alpha*(1-s)-beta*s)
    return s


def rnew(r_old, Vj):
    rj = []
    for i in range(0, numc):
        r_num = r_old[i] + dt*(1/taur - 1/taud)/(1+sy.exp(-Vj[i]+V0))
        r_den = 1 + dt*((1/taur - 1/taud)/(1+sy.exp(-Vj[i]+V0)) + 1/taud)
        rji = r_num/r_den
        rj.append(rji)
    return rj

def izero(t):
    if(t1p<t) and (t<t2p):
        i=ip; #i=ip when t1p<t<t2p
    else:
        i=0
    return i



VS = sy.IndexedBase('VS', numc)
var = []
for i in range(numc):
    var.append(VS[i])

rj = sy.Matrix(rnew([1, 2, 3], var))
s = sy.solve(rj, var)

real_solutions = np.fromiter((sy.re(value) for value in s.values()), dtype=float)

print(real_solutions)


