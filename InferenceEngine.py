import numpy as np


class inference_enginge:
    def __init__(self):
        self.Rulls = []

    def add_rull(self, A1, A2, B):
        A1_ExtendOn_x2 = np.resize(A1, (A2.shape[0], A1.shape[0]))
        A2_ExtendOn_x1 = (np.resize(A2, (A1.shape[0], A2.shape[0]))).T
        B_ExtendOn_x1_x2 = (np.resize(B, (A1.shape[0], A2.shape[0], B.shape[0]))).T
        self.Rulls.append([A1_ExtendOn_x2, A2_ExtendOn_x1, B_ExtendOn_x1_x2])
        

    def Product(self, A_prime):
        B_primes = []
        for i in range(len(self.Rulls)):
            B_primes.append(
                np.max(
                    (self.Rulls[i][0] * self.Rulls[i][1] * A_prime) * self.Rulls[i][2],
                    axis=1,
                ).max(axis=1)
            )
        return B_primes

    def Minimum(self, A_prime):
        B_primes = []
        for i in range(len(self.Rulls)):
            Min_A = np.resize(
                np.minimum(np.minimum(self.Rulls[i][0], self.Rulls[i][1]), A_prime),
                self.Rulls[i][2].shape,
            )
            B_primes.append(
                np.max(np.minimum(Min_A, self.Rulls[i][2]), axis=1).max(axis=1)
            )
        return B_primes

    def Lukasiewics(self, A_prime):
        B_primes = []
        for i in range(len(self.Rulls)):
            Min_Ai = np.minimum(self.Rulls[i][0], self.Rulls[i][1])
            A_prime_extended = np.resize(A_prime, self.Rulls[i][2].shape)
            B_primes.append(
                np.max(
                    np.minimum(1 - Min_Ai + self.Rulls[i][2], A_prime_extended), axis=1
                ).max(axis=1)
            )
        return B_primes

    def Zadeh(self, A_prime):
        B_primes = []
        for i in range(len(self.Rulls)):
            Min_Ai = np.resize(
                np.minimum(self.Rulls[i][0], self.Rulls[i][1]), self.Rulls[i][2].shape
            )
            A_prime_extended = np.resize(A_prime, self.Rulls[i][2].shape)
            B_primes.append(
                np.max(
                    np.minimum(
                        np.maximum(np.minimum(Min_Ai, self.Rulls[i][2]), 1 - Min_Ai),
                        A_prime_extended,
                    ),
                    axis=1,
                ).max(axis=1)
            )
        return B_primes

    def Dienes_Rescher(self, A_prime):
        B_primes = []
        for i in range(len(self.Rulls)):
            Min_Ai = np.resize(
                np.minimum(self.Rulls[i][0], self.Rulls[i][1]), self.Rulls[i][2].shape
            )
            A_prime_extended = np.resize(A_prime, self.Rulls[i][2].shape)
            B_primes.append(
                np.max(
                    np.minimum(
                        np.maximum(1 - Min_Ai, self.Rulls[i][2]), A_prime_extended
                    ),
                    axis=1,
                ).max(axis=1)
            )
        return B_primes
