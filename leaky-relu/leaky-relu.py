import numpy as np

def leaky_relu(x, alpha=0.01):
    x = np.array(x, dtype=float)

    # l = len(x)

    # for i in range(l):
    #     if x[i] < 0:
    #         x[i] = alpha * x[i]

    # return x

    return np.maximum(alpha * x, x)