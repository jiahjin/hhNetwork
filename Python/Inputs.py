# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:14:30 2023

@author: 12018
"""
import numpy as np
import sympy as sy
from ocrate import *

# nxnsynaptic adjacency matrix
a = np.array([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])
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
ENa = 55; #(mV)
#K+ equilibrium potential:
EK = -72; #(mV)
#leakage channel reversal potential:
EL = -49; #(mV)
#maximum specific conductance:
gcbar = 0.4;

#initialize time step and experiment duration:
dt=0.1; #time step duration (ms)
tmax=30; #duration of experiment (ms)
#total number of time steps in the experiment:
klokmax= np.ceil(tmax/dt); #round up to integer

#initialize arrays that hold data for plotting:
mhn_plot=[]
v_plot=np.empty((int(klokmax),numc))
# v_plot = []
t_plot=[]

#initialize parameters that define the experiment:
#the neuron is at rest (v= -70 mV) prior to t=O;
#at t=O a current shock is applied after which v= -55 mV;
#voltage prior to t=O:
vhold=np.array( [-70 for _ in range(numc)])
#voltage just after t=O:
#vstart= -55; %(mV)
vstart= np.array([-55 for _ in range(numc)])
v = vhold
#(change in v is result of current shock applied at t=O)

#simulate time prior to t=O: 

#set m,h,n equal to their steady values
#under constant-v conditions:

# print(alpham(v))
betam(v)
m = alpham(v)/(alpham(v)+betam(v))
h = alphah(v)/(alphah(v)+betah(v))
n = alphan(v)/(alphan(v)+betan(v))


# compute initial r
taur = 0.5;
taud = 8; 
V0 = 20;
Vsyn = 20
ri = 1-1/taud/(1+np.exp(-v+V0));
r = ri

#now let voltage jump to its value
#just after t=O, without making
#any further change in m,h,n:
v=vstart;

#then a subsequent 15 muA current pulse of 1 ms duration
#is applied beginning at t=lO ms.
def poisrand(n,lamb):
    poisrand = np.empty(n)
    
    for i in range(n):
        xt = 0
        t = 0
        while t<1:
            x = xt
            y = -(1/lamb)*np.log(1-np.random.uniform())
            t = t+y
            xt = xt+1
        poisrand[i] = x
    return poisrand
lamb = 10
t1p=poisrand(numc,lamb) #starting time (ms)
# t2p=t1p+0.5; #stopping time (ms) 
ip=50;  #current applied (muA) 

def izero(t,t1p):
    t2p=t1p+0.5
    if(t1p<t) and (t<t2p):
        i=ip; #i=ip when t1p<t<t2p
    else:
        i=0
    return i

# def izero(t):
#     iz = np.zero(numc)
#     for i in range(numc)
#         if(t1p[i]<t) and (t<t2p[i]):
#         i=ip; #i=ip when t1p<t<t2p
#     else:
#         i=0
#     return i


def snew(s_old, alpha, beta, dt):
    k1 = alpha*(1-s_old)-beta*(s_old)
    k2 = alpha*(1-(s_old+0.5*dt*k1))-beta*(s_old+0.5*dt*k1)
    k3 = alpha*(1-(s_old+0.5*dt*k2))-beta*(s_old+0.5*dt*k2)
    k4 = alpha*(1-(s_old+dt*k3))-beta*(s_old+dt*k3)
    s = s_old + (dt/6)*(k1+2*k2+2*k3+k4)
    
    
    
    # s =(s_old+dt*alpha)/(1+dt*(alpha+beta))
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
    rj = np.array(rj).astype(float)
    return rj


#initialize checking parameter
check=1
#set check=l to enable self-checking
#set check=O to disable self-checking 

# VS = sy.IndexedBase('VS', numc)
# var = []
# eqn =[0]*numc
# for i in range(numc):
#     var.append(VS[i])
#     eqn[i] = VS[i]-5

# s = sy.solve(eqn, var)
# print(s)

# real_solutions = np.fromiter((sy.re(value) for value in s.values()), dtype=float)

# print(real_solutions)



