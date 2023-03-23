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

# rr = [-70,-70,-70]
# mm = alpham(rr)/(alpham(rr)+betam(rr))
# print(mm)
# print(snew(m,o.alpham(v),o.betam(v),dt))
# print(alpham(v))



# for klok in range (int(klokmax)):
for klok in range (1):
    t=(klok+1)*dt;
    for i in range(numc):
        m=snew(m,o.alpham(v),o.betam(v),dt) #update m
        h=snew(h,o.alphah(v),o.betah(v),dt) #update h
        n=snew(n,o.alphan(v),o.betan(v),dt) #update n
        gNa = gNabar*(m**3)*h   #sodium conductance
        gK = gKbar*(n**4)   #potassium conductance
        g = gNa+gK+gLbar    #total conductance
        gE=gNa*ENa+gK*EK+gLbar*EL;
        print(gE)


    #     h[i]=snew(h,o.alphah(v[i]),o.betah(v[i]),dt)
    #     n=snew(n,o.alphan(v[i]),o.betan(v[i]),dt)
    #     gNa = gNabar*(m**3)*h   #sodium conductance
    #     gK = gKbar*(n**4)   #potassium conductance
    #     g = gNa+gK+gLbar    #total conductance
    #     gE=gNa*ENa+gK*EK+gLbar*EL; #gE=g•E   
    #     rj = rnew(r,VS)
    #     Isyn = gcbar*(Vsyn-VS[i])*sum(a[i, :]*rj)
    #     eqn.append(VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i]))
    # return eqn
        
    # VS = np.array([0,0,0]) #will be replaced
    # def equations(VS):
    #     eqn = []
    #     for i in range(numc):
            # m=snew(m,o.alpham(v[i]),o.betam(v[i]),dt) #update m
            # h=snew(h,o.alphah(v[i]),o.betah(v[i]),dt) #update h
            # n=snew(n,o.alphan(v[i]),o.betan(v[i]),dt) #update n
            # gNa = gNabar*(m**3)*h   #sodium conductance
            # gK = gKbar*(n**4)   #potassium conductance
            # g = gNa+gK+gLbar    #total conductance
            # gE=gNa*ENa+gK*EK+gLbar*EL; #gE=g•E   
    #         rj = rnew(r,VS)
    #         Isyn = gcbar*(Vsyn-VS[i])*sum(a[i, :]*rj)
    #         eqn.append(VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i]))
    #     return eqn
    # v= fsolve(equations, VS)
    # print(v)
    # r = rnew(r,v)
    
    

    # mm = [-53.16983875, -53.16983875, -52.907772  ]
    # print(float(equations(mm)))
    # for i in range(numc):
        # m=snew(m,o.alpham(v[i]),o.betam(v[i]),dt) #update m
        # h=snew(h,o.alphah(v[i]),o.betah(v[i]),dt) #update h
        # n=snew(n,o.alphan(v[i]),o.betan(v[i]),dt) #update n
        # gNa = gNabar*(m**3)*h   #sodium conductance
        # gK = gKbar*(n**4)   #potassium conductance
        # g = gNa+gK+gLbar    #total conductance
        # gE=gNa*ENa+gK*EK+gLbar*EL; #gE=g•E
        # v_old = v;

        
        # VS = np.array([0,0,0]) #will be replaced
        
        # VS = sy.IndexedBase('VS',numc)
        # VS = sy.sym
    #     x, y, z = sy.symbols('x, y, z', real = True)
    #     VS = [x,y,z]
    #     rj = rnew(r,VS)
    #     Isyn = gcbar*(Vsyn-VS[i])*sum(a[i, :]*rj)
    #     eqn.append(VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i]))

    # VG = np.array([0,0,0])  
    # print(eqn)
    # v= fsolve(eqn, VG)
    # print(v)

        
    #     def equations(VS):
    #         eqn = []
    #         for i in range(numc):
    #             Isyn = gcbar*(Vsyn-VS[i])*sum(a[i, :]*rj)
    #             eqn.append(VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i]))
    #         return eqn

    #     mm = [-53.16983875, -53.16983875, -52.907772  ]
    #     print(float(equations(mm)))
  
    # v = fsolve(equations, VS)
    # print(v)
    # r = rnew(r,v)
    # v1 = np.array(v[0])
    # print(v[1])
    # print(v1)
    # print(t)
    # v_plot = np.zeros((3,10))
    # for i in range(numc):
    #     for j in range(1,10):
    #         v_plot[i][j] = v1[j][i]
    # t_plot[klok] = t
    
    # plot(t_plot,v_plot(1,:),t_plot, v_plot(2,:), t_plot,v_plot(3,:))

    # hold on
    # % subplot(2,1,1),plot(t_plot,v_plot)
    #      for i = 1:numc
    #         plot(t_plot,v_plot(i,:));
    
    #      end
    # hold off;
    # print(v) 
    # t = np.array(t)
    # tT = t.T
    # tT = t.T()
    # vT = v1.T()
# print(tT)
# plt.figure()
# plt.plot(tT, v1.T)
    # plt.show()

        
        #symbol
    #     VS = sy.IndexedBase('VS',numc)
    #     var = []
    #     var.append(VS[i])
        
    #     #equations
    #     eqn =[0]*numc
    #     rj = rnew(r,VS)
    #     Isyn = gcbar*(20-VS[i])*sum(a[i, :]*rj)
    #     eqn[i] = VS[i]-(v[i]+(dt/C)*(gE[i]+izero(t)+Isyn))/(1+(dt/C)*g[i])
        
    # sol = sy.solve(eqn,var)
    # print(sol)
    # v = np.array([sol[key].evalf() for key in sol.keys()], dtype=float)

    # print(v)
    # r = rnew(r,v);
    
#  def equations(x):
#     # Define your system of equations here
#     eq1 = x[0] + x[1] - 3
#     eq2 = x[0]**2 + x[1]**2 - 9
#     return [eq1, eq2]


           

#         f1 = VS[0]-2*VS[1]
#         f2 = VS[0]+VS[1]-3

#         system = [f1, f2]
#         jj= sy.solve(system, var)
#         print(jj)
#         vs = sp.symbol('k', integer=True)
#         VS = [vs]*numc

#         VS = sy.symbols('VS',[1,numc]); #Symbol for V
#         # update v:
#         for i in range(numc):
#             rj = rnew(r,VS)
#             ar = a #aij*rj(t)*(Vsyn-Vi)
#             sumarv = 
# %update v:
# for i = 1: numc
#     rj = rnew(r,VS);
#     arv = a(i, :).*rj.*(20-VS);
#     sumarv = sum(arv(i));
#     Isyn = gcbar*sumarv;
#     eqn(i) = VS(i)==(v(i)+(dt/C)*(gE(i)+izero(t)+Isyn))/(1+(dt/C)*g(i));
# end
        
# y, z = symbols('y, z', real = True) # y = angle between r_cb and x-axis, z = output angle
# i = symbol('i', integer=True)
            