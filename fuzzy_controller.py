import numpy as np
from InferenceEngine import inference_enginge_wheel
from Fuzzify import Fuzzifier_wheel
from Defuzzify import Defuzzifier


class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        X_lr = np.linspace(0, 100, num=101)
        Wheel = np.linspace(-50, 50, num=101)

        CLOSE_lr = -1 / 50 * X_lr + 1
        CLOSE_lr = np.where(CLOSE_lr < 0, 0, CLOSE_lr)

        MODERATE_lr = X_lr.copy()
        MODERATE_lr[X_lr <= 50] = (X_lr[X_lr <= 50] - 35) / 15
        MODERATE_lr[X_lr > 50] = -(X_lr[X_lr > 50] - 65) / 15
        MODERATE_lr = np.where(MODERATE_lr < 0, 0, MODERATE_lr)

        FAR_lr = 1 / 50 * X_lr - 1
        FAR_lr = np.where(FAR_lr < 0, 0, FAR_lr)

        HIGH_r = Wheel.copy()
        HIGH_r[Wheel <= -20] = (Wheel[Wheel <= -20] + 50) / 30
        HIGH_r[Wheel > -20] = -(Wheel[Wheel > -20] + 5) / 15
        HIGH_r = np.where(HIGH_r < 0, 0, HIGH_r)

        LOW_r = Wheel.copy()
        LOW_r[Wheel <= -10] = (Wheel[Wheel <= -10] + 20) / 10
        LOW_r[Wheel > -10] = -(Wheel[Wheel > -10]) / 10
        LOW_r = np.where(LOW_r < 0, 0, LOW_r)

        Nothing = Wheel.copy()
        Nothing[Wheel <= 0] = (Wheel[Wheel <= 0] + 10) / 10
        Nothing[Wheel > 0] = -(Wheel[Wheel > 0] - 10) / 10
        Nothing = np.where(Nothing < 0, 0, Nothing)

        LOW_l = Wheel.copy()
        LOW_l[Wheel <= 10] = (Wheel[Wheel <= 10]) / 10
        LOW_l[Wheel > 10] = -(Wheel[Wheel > 10] - 20) / 10
        LOW_l = np.where(LOW_l < 0, 0, LOW_l)

        HIGH_l = Wheel.copy()
        HIGH_l[Wheel <= 20] = (Wheel[Wheel <= 20] - 5) / 15
        HIGH_l[Wheel > 20] = -(Wheel[Wheel > 20] - 50) / 30
        HIGH_l = np.where(HIGH_l < 0, 0, HIGH_l)

        self.Engine = inference_enginge_wheel()
        self.Engine.add_rull(CLOSE_lr, MODERATE_lr, LOW_r)
        self.Engine.add_rull(CLOSE_lr, FAR_lr, HIGH_r)
        self.Engine.add_rull(MODERATE_lr, CLOSE_lr, LOW_l)
        self.Engine.add_rull(FAR_lr, CLOSE_lr, HIGH_l)
        self.Engine.add_rull(MODERATE_lr, MODERATE_lr, Nothing)

        self.Fuzzifier = Fuzzifier_wheel(X_lr.copy(), X_lr.copy())
        self.Defuzzifier = Defuzzifier(Wheel.copy())

    def decide(self, left_dist, right_dist):
        A_prime = self.Fuzzifier.Min_Triangular(left_dist, right_dist, 10, 10)
        B_primes = self.Engine.Lukasiewics(A_prime.copy())

        return self.Defuzzifier.MeanOfMaxima_min(B_primes)
