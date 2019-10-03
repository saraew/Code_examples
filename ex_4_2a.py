# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:54:57 2019

@author: sara_
"""

import numpy as np              
import numpy.linalg as la   
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  # For 3-d plot
from matplotlib import cm 
import scipy as sc
from scipy.integrate import odeint
from matplotlib import animation

r = 0.5
a = 1
#Plotte xi mot r?

def xi_wendroff(x):
    R = (1-r)/(1+r)
    a = (1+(R**2)+2*R*np.cos(x))**(-2)
    b = (2*R + (1+(R**2))*np.cos(x))**2
    c = (((R**2)-1)*np.sin(x))**2
    return np.sqrt(a*(b+c))

def a_wendroff(x):
    R = (1-r)/(1+r)
    b = 2*R + (1+(R**2))*np.cos(x)        #Re
    c = ((R**2)-1)*np.sin(x)              #Im
    return np.arctan(-c/b)/(x*(r/a))

def xi_lax(x):
    return np.sqrt(1-(4*r**2)*(1-r**2)*(np.sin(x/2))**4)

def a_lax(x):
    y = np.arctan((r*np.sin(x))/(1-(2*r**2)*(np.sin(x/2))**2))
    return y/(x*(r/a))

x = np.linspace(-np.pi, np.pi, 100)

fig = plt.figure(1)
plt.plot(x, xi_wendroff(x), color = "red", label = "W")
plt.plot(x, xi_lax(x), color = "orange", label = "LW")
plt.axvline(x=0.2513, color = "black")
plt.xlabel(r"$\beta h$")
plt.ylabel(r"$\xi$")
plt.title("Dissipation")
plt.legend()
plt.show()

fig = plt.figure(2)
plt.plot(x, a_wendroff(x), color = "red", label = "W")
plt.plot(x, a_lax(x), color = "orange", label = "LW")
plt.axvline(x=0.2513, color = "black")
plt.xlabel(r"$\beta h$")
plt.ylabel(r"$\alpha$")
plt.title("Dispersion")
plt.legend()
plt.show()