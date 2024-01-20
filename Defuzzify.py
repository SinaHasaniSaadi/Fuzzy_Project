import numpy as np
import matplotlib.pyplot as plt


class Defuzzifier:
    def __init__(self, y):
        self.y = y

    def Center_Average(self, B_primes):
        sum1 = 0
        sum2 = 0
        for B_prime in B_primes:
            height = np.max(B_prime)
            ind_center = np.mean(np.where(B_prime == height)[0]).astype(int)
            sum1 += height * self.y[ind_center]
            sum2 += height
        return sum1 / (sum2 + 0.0001)

    def Centeroid_Max(self, B_primes, alpha=0):
        Max = B_primes[0]
        for B_prime in B_primes:
            Max = np.maximum(B_prime, Max)
        cut = Max[Max > alpha]
        cut_ind = np.where(Max > alpha)[0]
        if cut_ind.shape[0] != 0:
            return np.trapz(self.y[cut_ind] * cut, x=self.y[cut_ind]) / (
                np.trapz(cut, x=self.y[cut_ind]) + 0.0001
            )
        else:
            return 0

    def Centeroid_Min(self, B_primes, alpha=0):
        Min = B_primes[0]
        for B_prime in B_primes:
            Min = np.minimum(B_prime, Min)
        cut = Min[Min > alpha]
        cut_ind = np.where(Min > alpha)[0]
        if cut_ind.shape[0] != 0:
            return np.trapz(self.y[cut_ind] * cut, x=self.y[cut_ind]) / (
                np.trapz(cut, x=self.y[cut_ind]) + 0.0001
            )
        else:
            return 0

    def MeanOfMaxima_max(self, B_primes):
        Max = B_primes[0]
        for B_prime in B_primes:
            Max = np.maximum(B_prime, Max)
        return ((self.y[np.where(Max == Max.max())[0]]).mean()).astype(int)

    def MeanOfMaxima_min(self, B_primes):
        Min = B_primes[0]
        for B_prime in B_primes:
            Min = np.minimum(B_prime, Min)
        return ((self.y[np.where(Min == Min.max())[0]]).mean()).astype(int)
