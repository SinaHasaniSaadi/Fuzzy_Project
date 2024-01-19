import numpy as np
from InferenceEngine import inference_enginge_gas
from Fuzzify import Fuzzifier_gas
from Defuzzify import Defuzzifier


class FuzzyGasController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        X_c = np.linspace(0, 200, num=201)
        Gas = np.linspace(0, 90, num=91)

        Close = -1 / 50 * X_c + 1
        Close = np.where(Close < 0, 0, Close)

        Moderate = X_c.copy()
        Moderate[X_c <= 50] = (X_c[X_c <= 50] - 40) / 10
        Moderate[X_c > 50] = -(X_c[X_c > 50] - 100) / 50
        Moderate = np.where(Moderate < 0, 0, Moderate)

        Far = (X_c - 90) / 110
        Far = np.where(Far < 0, 0, Far)

        Low = Gas.copy()
        Low[Gas <= 5] = (Gas[Gas <= 5]) / 5
        Low[Gas > 5] = -(Gas[Gas > 5] - 10) / 5
        Low = np.where(Low < 0, 0, Low)

        Medium = Gas.copy()
        Medium[Gas <= 15] = (Gas[Gas <= 15]) / 15
        Medium[Gas > 15] = -(Gas[Gas > 15] - 30) / 15
        Medium = np.where(Medium < 0, 0, Medium)

        High = Gas.copy()
        High[Gas <= 30] = (Gas[Gas <= 30] - 25) / 5
        High[High > 30] = -(Gas[Gas > 30] - 90) / 60
        High = np.where(High < 0, 0, High)

        self.Engine = inference_enginge_gas()
        self.Engine.add_rull(Close, Low)
        self.Engine.add_rull(Moderate, Medium)
        self.Engine.add_rull(Far, High)

        self.Fuzzifier = Fuzzifier_gas(X_c.copy())
        self.Defuzzifier = Defuzzifier(Gas.copy())

    def decide(self, center_dist):
        A_prime = self.Fuzzifier.Singeleton(center_dist)
        B_primes = self.Engine.Lukasiewics(A_prime.copy())
        return self.Defuzzifier.MeanOfMaxima_min(B_primes)
