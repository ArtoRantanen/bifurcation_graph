import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)


#x(n+1) = r*x(n)*(1 - x(n))
xax = []
yax = []
r = 2.9
x_prev = 0.3
x = 0
min = 5
max = 0
for year in range(50):
    x = x_prev*r*(1-x_prev)
    xax.append(year)
    yax.append(x)
    x_prev = x
    if x_prev > max:
        max = x_prev
    if x_prev < min:
        min = x_prev

ax1.plot(xax, yax, marker='o', color='b')
ax1.set_ylim(min, max)
ax1.set_xlabel('year')
ax1.set_ylabel('population')
ax1.set_title('r=' + str(r))
ax1.grid(color='black', linewidth=2, linestyle='--')
plt.show()

