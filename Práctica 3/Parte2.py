import numpy as np
from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.io import loadmat

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def testClassificator(h, Y):
    aciertos = 0
    for i in range (h.shape[0]):
        max = np.argmax(h[i])

        max += 1

        if max == Y[i]:
            aciertos += 1

    precision = (aciertos / h.shape[0]) * 100
    print("La precisión es del", precision)


def forward_propagate(X, theta1, theta2):
    m = X.shape[0] 

    a1 = np.hstack([np.ones([m, 1]), X])    # (5000, 401)
    z2 = np.dot(a1, theta1.T)   # (5000, 25)

    a2 = np.hstack([np.ones([m, 1]), sigmoid(z2)])  # (5000, 26)
    z3 = np.dot(a2, theta2.T)   # (5000, 10)

    h = sigmoid(z3) # (5000, 10)

    return a1, z2, a2, z3, h


def main():
    data = loadmat("ex3data1.mat")
    Y = data["y"] # Y (5000, 1)
    X = data["X"] # X (5000, 400)

    weights = loadmat("ex3weights.mat")
    theta1, theta2 = weights["Theta1"], weights["Theta2"]
    # Theta1 es de dimensión 25 x 401
    # Theta2 es de dimensión 10 x 26

    delta1 = np.zeros(theta1.shape)
    delta2 = np.zeros(theta2.shape)

    a1, z2, a2, z3, h = forward_propagate(X, theta1, theta2)

    testClassificator(h, Y)

main()