import InferenceEngine_wheel
import numpy as np

X1 = np.linspace(0, 100, num=10000)
X2 = np.linspace(0, 100, num=10000)
WHEEL = np.linspace(-50, 50, num=10000)

CLOSE_L = -1 / 50 * X1 + 1
CLOSE_L = np.where(CLOSE_L < 0, 0, CLOSE_L)

MODERATE_L = X1.copy()
MODERATE_L[X1 <= 50] = (X1[X1 <= 50] - 35) / 15
MODERATE_L[X1 > 50] = -(X1[X1 > 50] - 65) / 15
MODERATE_L = np.where(MODERATE_L < 0, 0, MODERATE_L)

FAR_L = 1 / 50 * X1 - 1
FAR_L = np.where(FAR_L < 0, 0, FAR_L)

CLOSE_R = -1 / 50 * X2 + 1
CLOSE_R = np.where(CLOSE_R < 0, 0, CLOSE_R)

MODERATE_R = X2.copy()
MODERATE_R[X2 <= 50] = (X2[X2 <= 50] - 35) / 15
MODERATE_R[X2 > 50] = -(X2[X2 > 50] - 65) / 15
MODERATE_R = np.where(MODERATE_R < 0, 0, MODERATE_R)

FAR_R = 1 / 50 * X2 - 1
FAR_R = np.where(FAR_R < 0, 0, FAR_R)

HIGH_R = WHEEL.copy()
HIGH_R[WHEEL <= -20] = (WHEEL[WHEEL <= -20] + 50) / 30
HIGH_R[WHEEL > -20] = -(WHEEL[WHEEL > -20] + 5) / 15
HIGH_R = np.where(HIGH_R < 0, 0, HIGH_R)

LOW_R = WHEEL.copy()
LOW_R[WHEEL <= -10] = (WHEEL[WHEEL <= -10] + 20) / 10
LOW_R[WHEEL > -10] = -(WHEEL[WHEEL > -10]) / 10
LOW_R = np.where(LOW_R < 0, 0, LOW_R)

NOTHING = WHEEL.copy()
NOTHING[WHEEL <= 0] = (WHEEL[WHEEL <= 0] + 10) / 10
NOTHING[WHEEL > 0] = -(WHEEL[WHEEL > 0] - 10) / 10
NOTHING = np.where(NOTHING < 0, 0, NOTHING)

LOW_L = WHEEL.copy()
LOW_L[WHEEL <= 10] = (WHEEL[WHEEL <= 10]) / 10
LOW_L[WHEEL > 10] = -(WHEEL[WHEEL > 10] - 20) / 10
LOW_L = np.where(LOW_L < 0, 0, LOW_L)

HIGH_L = WHEEL.copy()
HIGH_L[WHEEL <= 20] = (WHEEL[WHEEL <= 20] - 5) / 15
HIGH_L[WHEEL > 20] = -(WHEEL[WHEEL > 20] - 50) / 30
HIGH_L = np.where(HIGH_L < 0, 0, HIGH_L)


class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.Engine = InferenceEngine_wheel.inference_enginge()

    def decide(self, left_dist, right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        return 0
