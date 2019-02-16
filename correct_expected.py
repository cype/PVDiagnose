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
    :return: correct expectation with efficiency of the pv installation
    """

    return float(peak_power) / area
