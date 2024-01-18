import numpy as np


class Fuzzifier_wheel:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def Singeleton(self, x1s, x2s):
        A_prime = np.zeros((self.x2.shape[0], self.x1.shape[0]))
        ind_x1 = np.argmin(np.abs(x1s - self.x1))
        ind_x2 = np.argmin(np.abs(x2s - self.x2))
        A_prime[ind_x2][ind_x1] = 1
        return A_prime

    def Min_Guassian(self, x1s, x2s, a1, a2):
        x1s = self.x1[np.argmin(np.abs(self.x1 - x1s))]
        x2s = self.x2[np.argmin(np.abs(self.x2 - x2s))]
        A1_p = np.resize(
            np.exp(-((self.x1 - x1s) ** 2) / a1**2),
            (self.x2.shape[0], self.x1.shape[0]),
        )
        A2_p = np.resize(
            np.exp(-((self.x2 - x2s) ** 2) / a2**2),
            (self.x1.shape[0], self.x2.shape[0]),
        ).T
        return np.minimum(A1_p, A2_p)

    def Product_Guassian(self, x1s, x2s, a1, a2):
        x1s = self.x1[np.argmin(np.abs(self.x1 - x1s))]
        x2s = self.x2[np.argmin(np.abs(self.x2 - x2s))]
        A1_p = np.resize(
            np.exp(-((self.x1 - x1s) ** 2) / a1**2),
            (self.x2.shape[0], self.x1.shape[0]),
        )
        A2_p = np.resize(
            np.exp(-((self.x2 - x2s) ** 2) / a2**2),
            (self.x1.shape[0], self.x2.shape[0]),
        ).T
        return A1_p * A2_p

    def Min_Triangular(self, x1s, x2s, b1, b2):
        x1s = self.x1[np.argmin(np.abs(self.x1 - x1s))]
        x2s = self.x2[np.argmin(np.abs(self.x2 - x2s))]
        a1 = np.resize(
            1 - np.abs(self.x1 - x1s) / b1,
            (self.x2.shape[0], self.x1.shape[0]),
        )
        a1 = np.maximum(0, a1)
        a2 = np.resize(
            1 - np.abs(self.x2 - x2s) / b2, (self.x1.shape[0], self.x2.shape[0])
        ).T
        a2 = np.maximum(0, a2)
        return np.minimum(a1, a2)

    def Product_Triangular(self, x1s, x2s, b1, b2):
        x1s = self.x1[np.argmin(np.abs(self.x1 - x1s))]
        x2s = self.x2[np.argmin(np.abs(self.x2 - x2s))]
        a1 = np.resize(
            1 - np.abs(self.x1 - x1s) / b1,
            (self.x2.shape[0], self.x1.shape[0]),
        )
        a1 = np.maximum(0, a1)
        a2 = np.resize(
            1 - np.abs(self.x2 - x2s) / b2, (self.x1.shape[0], self.x2.shape[0])
        ).T
        a2 = np.maximum(0, a2)
        return a1 * a2

class Fuzzifier_gas:
    def __init__(self, x):
        self.x = x

    def Singeleton(self, xs):
        A_prime = np.zeros(self.x.shape[0])
        ind_x = np.argmin(np.abs(xs - self.x))
        A_prime[ind_x] = 1
        return A_prime

    def Guassian(self, xs, a):
        xs = self.x[np.argmin(np.abs(self.x - xs))]
        A_p = np.exp(-((self.x - xs) ** 2) / a**2)
        return A_p

    def Triangular(self, xs, b):
        xs = self.x[np.argmin(np.abs(self.x - xs))]
        A_p = 1 - np.abs(self.x - xs) / b
        A_p = np.maximum(0, A_p)
        return A_p