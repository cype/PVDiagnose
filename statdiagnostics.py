import numpy as np
import matplotlib as plt
from scipy.stats import t

def pv_has_malfunction(area, expected, measured):
    """
    Tests if the deviation from the expected is significantly less than gamma0.
    expected and measured can have arbitrary length but they need to be of the same length.
    :param area: area covered by the pv in m^2
    :param expected: list of expected kWh/m^2 ordered by month
    :param measured: list of measured kWh values ordered by months the same way as expected
    :return: true if there is a malfunction
    """
    gamma0 = 0 # could also be a small negative number
    alpha = 0.05 # level of test
    ex = np.array(expected)*area
    me = np.array(measured)
    z = me-ex 
    if z.var() > 0:
        P = np.sqrt(len(measured))*(z.mean()-gamma0)/z.std(ddof=1)
        print(t.cdf(P, len(measured)-1))
        return P < t.ppf(alpha, len(measured)-1)
    else:
        return z.mean() < gamma0



