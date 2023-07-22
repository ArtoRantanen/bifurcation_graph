import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

plt.ion()
figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax2 = figure.add_subplot(2, 2, 2)

x_population = np.arange(1, 51, 1)
y_population = np.arange(0, 1, 0.02)
line_population, = ax1.plot(x_population, y_population, marker='o', color='b')
ax1.set_ylim(0, 1)
ax1.set_xlabel('year')
ax1.set_ylabel('population')
ax1.set_title('r=' + str(0))
ax1.grid(color='black', linewidth=1, linestyle='--')

x_bifurcation = [0]
y_bifurcation = [0]
line_bifurcation, = ax2.plot(x_bifurcation, y_bifurcation, marker='o', color='b', linewidth=0)
ax2.set_ylim(0, 1)
ax2.set_xlim(0, 4)
ax2.set_xlabel('r')
ax2.set_ylabel('peak')
ax2.set_title('bifurcation')
ax2.grid(color='black', linewidth=1, linestyle='--', mew=0.2)

#x(n+1) = r*x(n)*(1 - x(n))
for step in np.arange(0, 4, 0.01):
    all_vertices = []
    x_prev = 0.5
    y = [x_prev]
    for year in range(49):
        x = x_prev * step * (1 - x_prev)
        y.append(x)
        x_prev = x
        if year > 5:
            all_vertices.append(x_prev)
    previous_vertice = 0.5
    steps=1
    median = dict({1: [1, 0]})
    new_verticies = []
    for vertice in all_vertices:
        index = all_vertices.index(vertice)
        if steps > 1:
            for picks in median:
                if (((median[picks][1])-0.02)<=vertice) and (((median[picks][1])+0.02)>=vertice):
                    median[picks][1] = (vertice + (median[picks][1])*(median[picks][0]))/(median[picks][0]+1)
                    median[picks][0] = median[picks][0] + 1
                else:
                    if len(new_verticies)>=1:
                        for v in new_verticies:
                            if (vertice-0.02)<=v and (vertice+0.02)>=v:
                                pass
                            else:
                                new_verticies.append(vertice)
                                break
                    else:
                        new_verticies.append(vertice)
        else:
            median[1][1] = vertice
        steps += 1
    if len(new_verticies)>0:
        for v in new_verticies:
            for vert in new_verticies:
                if (vert*0.98)<=v and (vert*1.02)>=v and v!=vert:
                    new_verticies.remove(vert)
    if len(new_verticies)>0:
        for v in new_verticies:
            for vert in new_verticies:
                if (vert*0.98)<=v and (vert*1.02)>=v and v!=vert:
                    new_verticies.remove(vert)
    print(new_verticies)
    x_bifurcation.append(step)
    y_bifurcation.append(median[1][1])
    for i in new_verticies:
        x_bifurcation.append(step)
        y_bifurcation.append(i)








    ax1.set_title('r=' + str(round(step, 2)))
    line_bifurcation.set_xdata(x_bifurcation)
    line_bifurcation.set_ydata(y_bifurcation)
    line_population.set_ydata(y)

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.02)


plt.show()

