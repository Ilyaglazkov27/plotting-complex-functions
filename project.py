import matplotlib.pyplot as plt
import cmath
from math import sqrt

fig = plt.figure()


def f(x):
    y = x  # можно подставить любую функцию
    return y.real, y.imag


i = -10
a = 0
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('$X$', fontsize=20)
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')
while (i < 10):
    x = []
    y = []
    z = []
    x1 = -10
    x2 = []
    y2 = []
    z2 = []
    while x1 < 10:
        if x1 == 0 and i == 0:
            x1 += 0.05
            continue
        y1, z1 = f(complex(x1, i))
        x.append(x1)
        y.append(y1)
        z.append(z1)
        x2.append(0)
        y2.append(0)
        z2.append(0)
        x1 += 0.05
    a += 20
    ax.plot(x, y, z)
    plt.draw()
    plt.pause(0.00000000001)
    i += 0.05
plt.pause(100000)
