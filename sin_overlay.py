import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = plt.axes(xlim=(0, 7), ylim=(-2, 2))
ax.grid(color='black', linewidth=1, linestyle='--')
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 50, 1000)
    y = np.sin(np.pi * (x - 0.01 * i)) + np.sin(np.pi*x)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()