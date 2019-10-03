# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:42:48 2018

@author: sara_
"""
import numpy as np
#import math
#import matplotlib.pyplot as plt



def func(x):
    return np.sin(x)

def func3(x):
    return np.sin(np.pi*np.exp(3*x))
#
def func4(x):
    return np.sin(np.pi*np.exp(4*x))
#
def func5(x):
    return np.sin(np.pi*np.exp(5*x))


def midpoint(a,b,func,n):
    h = (b-a)/n
    midpoint = 0
    for i in range(n):
        midpoint += func(a + (h/2) + (i*h))
    midpoint *= h
    return midpoint



def romberg_integration(a,b,func,tol,n):
    table = np.zeros((n,n))
    T_1 = ((b-a)/2)*(func(a) + func(b))        
    temp = T_1
    table[0][0] = T_1
    #h_n = (b-a)/(2**(n))
    #print("h_n1:", h_n)
    for i in range(1, n):
        summen = 0
        h_n = (b-a)/(2**(i))
        for k in range(1,2**(i-1)):
            summen += func(a + (2*k - 1)*h_n)
        T_n = ((1/2)*temp) + (h_n*summen)
        temp = T_n
        table[i][0] = (1/2)*(T_n + midpoint(a,b,func,i))
#    for i in range(1,n):
#        summen = 0
#        h_nn = (b-a)/(i)
#        for j in range(1,n):
#            summen += func(a+h_nn*j)
#        T = ((b-a)/(i))*(1/2)*(func(a)+func(b)+(2*summen))
#        print("Dette er T:",T)
#        print("Dette er midpoint", midpoint(a,b,func,i))
#        table[i][0] = (1/2)*(T + midpoint(a,b,func,i))
#        
    for l in range(1,n):
        for r in range(1,l+1):
            #print(table, "andre løkke")
            table[l][r] = (1/((4**r) - 1))*((4**r * table[l][r-1])-(table[l-1][r-1]))
        if l > 2 and (table[l][l]-table[l][l-1] < tol):
            approx = table[l][l]
            return approx
    print("Dette fungerte ikke som det skulle")        
    return approx

print(romberg_integration(0,1,func5, 0.0001,10))
    