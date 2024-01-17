import numpy as np


class Fuzzyfier:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def Singeleton(self, x1s, x2s):
        A_prime = np.zeros((self.x2.shape[0], self.x1.shape[0]))
        ind_x1 = np.argmin(np.abs(x1s - self.x1))
        ind_x2 = np.argmin(np.abs(x2s - self.x2))
        A_prime[ind_x2][ind_x1] = 1
        return A_prime
