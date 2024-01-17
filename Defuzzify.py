import numpy as np


class Defuzzifier:
    def __init__(self, y):
        self.y = y

    def Center_Average(self, B_primes):
        sum1 = 0
        sum2 = 0
        for B_prime in B_primes:
            height = np.max(B_prime)
            ind_center=np.mean(np.where(B_prime==height)[0]).astype(int)
            sum1 += height * self.y[ind_center]
            sum2 += height
        return sum1 / (sum2+0.0001)
