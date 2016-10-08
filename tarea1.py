import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA, KernelPCA
import scipy.io


def parse_matlab(file_name):
    mat = scipy.io.loadmat(file_name)
    return mat["ans"]

def parse_data(file_name):
    dataset_file = open(file_name, "r")
    _data = []
    for row in dataset_file:
        x, y, z = row.split()
        _data.append([float(x), float(y), float(z)])
    dataset_file.close()
    return np.array(_data)


def plot(xs, ys, zs):
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(xs, ys, zs)
    plt.show()


def show_dr(method, components, file_name):
    if method == "pca":
        method_obj = PCA(n_components=components, svd_solver=svd_solver)
    else:#elif method == "kpca":
        method_obj = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
    np_data = parse_matlab(file_name)
    result = method_obj.fit_transform(np_data)
    xs = result[:, 0]
    n = len(xs)
    zeros = np.zeros(n)
    print "explained_variance_ratio:", method_obj.explained_variance_ratio_
    print "explained_variance:", method_obj.explained_variance_
    print "covariance:", method_obj.get_covariance()
    print "presicion:", method_obj.get_precision()
    if components == 1:
        plot(xs, zeros, zeros)
    elif components == 2:
        plot(xs, result[:, 1], zeros)
    else:
        plot(xs, result[:, 1], result[:, 2])


svd_solver = "full"
#show_dr("pca", 3, "intersect.mat")
print np.random.normal(loc=1500, scale=1500, size=20)
#mat = scipy.io.loadmat('swissroll.mat')
#print mat["ans"]
#data = parse_matlab("intersect.mat")
#plot(data[:,0],data[:,1],data[:,2])
