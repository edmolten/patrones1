import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

datasetFile = open("swissroll.dat", "r")
xs = []
ys = []
zs = []
for line in datasetFile:
    x, y, z = line.split()
    xs.append(float(x))
    ys.append(float(y))
    zs.append(float(z))

ax.scatter(xs, ys, zs)
plt.show()
