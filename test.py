import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()

fig, ax = plt.subplots()
ax.set_title('r=0')
ax.set_ylabel('population')
ax.set_xlabel('year')
ax.set_ylim(0, 1)


x = np.arange(1, 51, 1)
y = np.arange(0, 1, 0.02)
line, = ax.plot(x, y, marker='o', color='b')

for step in np.arange(0, 4, 0.01):
    r = step
    x_prev = 0.5
    y = [x_prev]
    for year in range(49):
        x = x_prev * r * (1 - x_prev)
        y.append(x)
        x_prev = x
    ax.set_title('r=' + str(round(step, 2)))
    line.set_ydata(y)

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)
#x(n+1) = r*x(n)*(1 - x(n))


plt.show()

