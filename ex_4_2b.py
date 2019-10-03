# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:12:16 2019

@author: sara_
"""

import numpy as np               
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  # For 3-d plot
from matplotlib import cm
from matplotlib import animation

def f(x):
    return np.exp(-64*((x-0.5)**2))*np.sin(32*np.pi*x)

def hyp(method, f):
    a = 1
    T = 2
    h = 1/200
    #h = 1/400
    k = 1/400
    M = int(1/h)
    N = int(1/k)
    r = a*(k/h)
    
    x = np.linspace(0, 3, M+1)
    t = np.linspace(0, T, N+1)
    U = np.zeros((M+1, N+1)) 
    U[0,:] = 0
    U[:,0] = f(x)
    
    if method == "LW":
        for n in range(N):
            U[1:-1,n+1] = U[1:-1,n] - (r/2)*(U[2:,n]-U[0:-2,n]) + ((r**2)/2)*(U[2:,n]-2*U[1:-1,n]+U[0:-2,n])
    elif method == "W":
        for m in range(1, M+1):
            for n in range(N):
                U[m, n+1] = U[m-1,n] - ((1-r)/(1+r))*(U[m-1, n+1] - U[m, n])
    
    return x, t, U

x, t, U = hyp("W", f)

#fig = plt.figure(1)
#ax = fig.gca(projection="3d")
#T, X = np.meshgrid(t, x)
#ax.plot_surface(T, X, U, cmap=cm.coolwarm)
#ax.view_init(azim=120)  # Rotate the figure
#plt.xlabel('t')
#plt.ylabel('x')
#ax.set_zlabel(r"u(x,t)")
#plt.title("Solution")
#plt.show()

#Animation
fig = plt.figure()
ax = plt.axes(xlim=(0, 3), ylim=(-1, 1))
line, = ax.plot([], [], lw=2, color = "red")
time_text = ax.text(0.03, 0.925, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text,

def animate(i):
    y = U[:,i]
    line.set_data(x, y)
    time_text.set_text('time = %.1f' % (2*(i/len(t))))
    return line, time_text,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(t), interval=20, blit=True)

plt.title("Animation")
plt.show()