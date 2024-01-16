import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n = 50
VX = np.linspace(-2.0, 2.0, n)
VY = np.linspace(-2.0, 2.0, n)
X,Y = np.meshgrid(VX, VY)
def f(x,y):
    return x**2-y**2

Z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.view_init(40, -30)
ax.plot_surface(X, Y, Z)
plt.show()