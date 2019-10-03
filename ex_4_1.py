# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:27:03 2019

@author: sara_
"""
import numpy as np              
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D  # For 3-d plot
from matplotlib import cm
from matplotlib import animation

newparams = {'figure.figsize': (8.0, 4.0), 'axes.grid': True,
             'lines.markersize': 8, 'lines.linewidth': 2,
             'font.size': 12}
plt.rcParams.update(newparams)

def hyperbolic(method, r=1):
    a = 1
    T = 2
    h = 1/160
    k = r*h
    M = int(1/h)
    N = int(1/k)
    
    x = np.linspace(0, 3, M+1)
    t = np.linspace(0, T, N+1)
    U = np.zeros((M+1, N+1)) 
    U[0,:] = 1
    
    if method == "FTBS":
        for n in range(N):
            U[1:-1, n+1] = U[1:-1, n] - r*(U[1:-1, n]-U[0:-2, n])
    elif method == "LW":
        for n in range(N):
            U[1:-1,n+1] = U[1:-1,n] - (r/2)*(U[2:,n]-U[0:-2,n]) + ((r**2)/2)*(U[2:,n]-2*U[1:-1,n]+U[0:-2,n])
    elif method == "W":
        for m in range(1, M+1):
            for n in range(N):
                U[m, n+1] = U[m-1,n] - ((1-r)/(1+r))*(U[m-1, n+1] - U[m, n])
    
    return x, t, U

x, t, U = hyperbolic("LW", r=0.5)


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
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 3), ylim=(-0.3, 1.5))
line, = ax.plot([], [], lw=2, color = "red")
time_text = ax.text(0.03, 0.925, '', transform=ax.transAxes)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text,

# animation function.  This is called sequentially
def animate(i):
    y = U[:,i]
    line.set_data(x, y)
    time_text.set_text('time = %.1f' % (2*(i/len(t))))
    return line, time_text,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(t), interval=20, blit=True)

plt.title("Animation")
plt.show()

