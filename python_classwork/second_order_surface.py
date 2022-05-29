import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure("second-order sutfaces")
ax = fig.add_subplot(121, projection='3d')
ax.set_title("hyperbolic paraboloid")

i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
x = y = np.linspace(-3, 3, 74)

ax = fig.add_subplot(122, projection='3d')
ax.set_title("elliptical parabaloid")

i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 + Y**2
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
x = y = np.linspace(-3, 3, 74)

plt.show()
