import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA, KernelPCA
from sklearn.manifold import Isomap, LocallyLinearEmbedding
import scipy.io


def parse_matlab(file_name):
    mat = scipy.io.loadmat(file_name)
    return mat["ans"]


def plot(xs, ys, zs):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(xs, ys, zs)
    plt.show()


def show_dr(method, components, file_name, kernel="poly"):
    if method == "pca":
        method_obj = PCA(n_components=components)
    elif method == "kpca":
        method_obj = KernelPCA(degree=5, n_components=components, kernel=kernel)
    elif method == "isomap":
        method_obj = Isomap(n_components=components)
    else:
        method_obj = LocallyLinearEmbedding(n_components=components)
    np_data = parse_matlab(file_name)
    result = method_obj.fit_transform(np_data)
    xs = result[:, 0]
    n = len(xs)
    zeros = np.zeros(n)
    if components == 1:
        plot(xs, zeros, zeros)
    elif components == 2:
        plot(xs, result[:, 1], zeros)
    else:
        plot(xs, result[:, 1], result[:, 2])

show_dr("kpca", 2, "helix.mat")
'''
np_data = parse_matlab("swissroll.mat")
result = PCA(n_components=3).fit_transform(np_data)
xs = result[:, 0]
n = len(xs)
zeros = np.zeros(n)
plot(xs, result[:, 1], result[:, 2])
'''