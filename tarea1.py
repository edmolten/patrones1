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
        method_obj = KernelPCA(n_components=components, kernel=kernel)
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

# show_dr("kpca", 2, "helix.mat", kernel="rbf")


def get_mv_dataset(pcnt):
    filenames = ["swissroll.mat", "brokenswissroll.mat", "helix.mat", "intersect.mat"]
    datasets = []
    missung_number = 3000/pcnt
    for filename in filenames:
        np_data = parse_matlab(filename)
        indexes = np.random.randint(3000, size=missung_number)
        for i in indexes:
            randvar = np.random.randint(3)
            np_data[i][randvar] = np.nan
        datasets.append(np_data)
    return datasets


def get_all_ms_datasets():
    all_dss = []
    for pcnt in [10, 20, 30, 40, 50]:
        all_dss.append(get_mv_dataset(pcnt))


