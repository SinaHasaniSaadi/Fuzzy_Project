import numpy as np


class Fuzzifier:
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
        a1 = np.resize(
            np.exp(-((self.x1 - x1s) ** 2) / a1**2),
            (self.x2.shape[0], self.x1.shape[0]),
        )
        a2 = np.resize(
            np.exp(-((self.x2 - x2s) ** 2) / a2**2),
            (self.x1.shape[0], self.x2.shape[0]),
        ).T
        return np.minimum(a1, a2)

    def Product_Guassian(self, x1s, x2s, a1, a2):
        x1s = self.x1[np.argmin(np.abs(self.x1 - x1s))]
        x2s = self.x2[np.argmin(np.abs(self.x2 - x2s))]
        a1 = np.resize(
            np.exp(-((self.x1 - x1s) ** 2) / a1**2),
            (self.x2.shape[0], self.x1.shape[0]),
        )
        a2 = np.resize(
            np.exp(-((self.x2 - x2s) ** 2) / a2**2),
            (self.x1.shape[0], self.x2.shape[0]),
        ).T
        return a1 * a2

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
