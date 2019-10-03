# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 15:03:55 2018

@author: sara_
"""
import numpy as np
import matplotlib.pyplot as plt


u_0 = 1/3
v_0 = 1


A_1 = [0]
A_2 = [[0,0],[1,0]] 
A_3 = [[0,0,0],[1/2,0,0],[-1,2,0]]
A_4 = [[0,0,0,0],[1/2,0,0,0],[0,1/2,0,0],[0,0,1,0]]
#print(A_1,A_2,A_3,A_4)
b_1 = [1]
b_2 = [1/2, 1/2]
b_3 = [1/6, 2/3, 1/6]
b_4 = [1/6, 1/3, 1/3, 1/6]

N_e = 12
t_f = 3
u_n = 1/3
v_n = 1
u_der = u_n - (2*u_n*v_n)
v_der = (-v_n) + (3*u_n*v_n)

y_0 = np.array([1/3,1])

def LV(y):
    u_n,v_n = y[0], y[1] 
    return np.array([u_n - 2*u_n*v_n, -v_n + 3*u_n*v_n])
 
def k3_1(del_t,y_n):
    return del_t*LV(y_n)

def k3_2(del_t,y_n, k3_1):
    return del_t*LV(y_n + (1/2*k3_1(del_t,y_n)))

def k3_3(del_t,y_n, k3_1, k3_2):
    return del_t*LV(y_n - k3_1(del_t,y_n) + 2*k3_2(del_t,y_n, k3_1))
            
            
def k4_1(del_t,y_n):
    return del_t*LV(y_n)

def k4_2(del_t,y_n, k4_1):
    return del_t*LV(y_n + (1/2*k4_1(del_t,y_n)))

def k4_3(del_t,y_n, k4_2):
    return del_t*LV(y_n + (1/2)*k4_2(del_t,y_n, k4_1))

def k4_4(del_t,y_n, k4_3):
    return del_t*LV(y_n + k4_3(del_t, y_n, k4_2))


def ERK1(y_0,t_f):
    liste = []
    for k in range(1, N_e+1):
        y_n = y_0
        del_t = t_f*(2**(-k))
        count = 0
        while count <= t_f:
            y_n = y_n + b_1[0]*(del_t*LV(y_n))
            count += del_t
        liste.append(y_n)
    return liste




def ERK2(y_0,t_f):
    liste = []
    for k in range(1, N_e+1):
        y_n = y_0
        del_t = t_f*(2**(-k))
        count = 0
        while count <= t_f:
            y_n = y_n + b_2[0]*(del_t*LV(y_n)) + b_2[1]*del_t*LV(y_n + (del_t*LV(y_n)))
            count += del_t
        liste.append(y_n)
    return liste 



def ERK3(y_0,t_f):
    liste = []
    for k in range(1, N_e+1):
        y_n = y_0
        del_t = t_f*(2**(-k))
        count = 0
        while count <= t_f:
            y_n = y_n + (b_3[0]*(k3_1(del_t,y_n))) + (b_3[1]*(k3_2(del_t,y_n,k3_1))) + (b_3[2]*(k3_3(del_t,y_n, k3_1,k3_2)))
            count += del_t
        #print(y_n)
        liste.append(y_n)
    return liste 


def ERK4(y_0,t_f):
    liste = []
    for k in range(1, N_e+1):
        y_n = y_0
        del_t = t_f*(2**(-k))
        count = 0
        while count <= t_f:
            y_n = y_n + b_4[0]*(k4_1(del_t,y_n)) + b_4[1]*(k4_2(del_t,y_n, k4_1)) + b_4[2]*(k4_3(del_t,y_n,k4_2) + b_4[3]*(k4_4(del_t,y_n,k4_3)))
            count += del_t
        liste.append(y_n)
    return liste 



def ERK4_ref(y_0,t_f):
    y_n = y_0
    del_t = 0.1*t_f*(2**(-N_e))
    count = 0
    while count <= t_f:
        y_n = y_n + b_4[0]*(k4_1(del_t,y_n)) + b_4[1]*(k4_2(del_t,y_n, k4_1)) + b_4[2]*(k4_3(del_t,y_n,k4_2) + b_4[3]*(k4_4(del_t,y_n,k4_3)))
        count += del_t
    return y_n 


#
def simulation(y_0, t_f):
    Y_ex = ERK4_ref(y_0, t_f) 
#    ERR = [[0 for x in range(N_e)] for y in range(4)]
    ERR = []
    #Y = [[0 for x in range(4)] for y in range(2)]
    ERK_1 = np.array(ERK1(y_0,t_f))
    ERR.append(abs(ERK_1-Y_ex))
    ERK_2 = np.array(ERK2(y_0,t_f))
    ERR.append(abs(ERK_2-Y_ex))
    ERK_3 = np.array(ERK3(y_0,t_f))
    ERR.append(abs(ERK_3-Y_ex))
    ERK_4 = np.array(ERK4(y_0,t_f))
    ERR.append(abs(ERK_4-Y_ex))
    EKK = np.zeros((4,12))
    for i in range(4):
        for j in range(12):
            EKK[i][j] = (ERR[i][j][0] + ERR[i][j][1])/2 
    return EKK
ERR = simulation(y_0,t_f)
print(ERR)
k = [1,2,3,4,5,6,7,8,9,10,11,12]

def visualization():
    plt.figure()#, figsize = (6,5))
    plt.loglog()
    plt.plot(k, ERR[0], label = "ERK1")
    plt.plot(k, ERR[1], label = "ERK2")
    plt.plot(k, ERR[2], label = "ERK3")
    plt.plot(k, ERR[3], label = "ERK4")
    plt.title("Error plotted at different k-values")
    plt.ylabel("Error")
    plt.xlabel("k-values")
    plt.legend()
    plt.show()
    
    return
visualization()
#
#def main_program():
#    return