import math

#pre: give a list
#post: returns the average of the list
def average(alist):
    aver = 0
    for n in alist:
        aver += n
    return aver / len(alist)


#pre: give the list
#post: returns the variance of the list
def std(alist):
    summe = 0
    aver = average(alist)
    for n in alist:
        summe += (n - aver)**2
    return math.sqrt(summe/(len(alist)-1))


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
    #alpha = 0.05 # level of test
    #0.95-quantiles of t-distribution of degrees 1 to 11  
    tinv = [-6.341, -2.920, -2.353, -2.132, -2.015, -1.943, -1.895, -1.860, -1.833, -1.812, -1.796] 
    ex = [area*e for e in expected]
    z = []
    for i in range(len(measured)):
       z.append(measured[i]-ex[i]) 
    if std(z) > 0:
        P = math.sqrt(len(measured))*(average(z)-gamma0)/std(z)
        return P < tinv[len(measured)-2]
    else:
        return average(z) < gamma0

def pv_has_malfunction_with_correction(area, peak_power, expected, measured):
    
    pv_efficiency = pv_compute_efficiency(area, peak_power)
    
    ex = pv_correct_expected(pv_efficiency, expected)
    me = measured

    return pv_has_malfunction(area, ex, me)

def pv_correct_expected(efficiency, expected):
    """
    :param expected: list of expected kWh/m^2 ordered by month
    :param efficiency: has to be provided by the user
    :return: correct expectation with efficiency of the pv installation
    """
    
    #assumed efficiency used in sonnendach.ch computation = 0.17%

    corrected = [value * float(efficiency) / 0.17 for value in expected]

    return corrected

def pv_compute_efficiency(area, peak_power):
    """
    :param area: m^2
    :param peak_power: has to be provided by the user in kWp
    :return: computed efficiency of pv installation
    """

    return float(peak_power) / area




