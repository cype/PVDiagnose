from statdiagnostics import pv_has_malfunction
from matplotlib import pyplot as plt

import pandas as pd

def test_statdiagnostics(area, expected_data, measured_data, months):

    #normalize data
    expected_data_normalized = [float(i)/sum(expected_data) for i in expected_data]
    measured_data_normalized = [float(i)/sum(measured_data) for i in measured_data]
    
    #plot expected data and measured data
    df_rearanged = pd.DataFrame({
        'reference' : [area * value for value in expected_data],
        'measured' : measured_data
        },index = months
    )
    df_rearanged.plot(kind='bar')
    plt.show()
    print('output =', pv_has_malfunction(area, expected_data, measured_data))
    
    #plot normalized expected data and normalizde measured data
    df_rearanged = pd.DataFrame({
        'reference normalized' : expected_data_normalized,
        'measured normalized' : measured_data_normalized
        },index = months
    )
    df_rearanged.plot(kind='bar')
    plt.show()
    print('normalized data: output =', pv_has_malfunction(1, expected_data_normalized, measured_data_normalized))
    
    #plot normalized expected data and perturbed normalizde measured data
    #perturb data:
    measured_data_normalized[5] /= 2
    measured_data_normalized[6] /= 2
    
    df_rearanged = pd.DataFrame({
        'reference normalized + perturbation' : expected_data_normalized,
        'measured normalized + perturbation' : measured_data_normalized
        },index = months
    )
    df_rearanged.plot(kind='bar')
    plt.show()
    print('normalized data + perturbation: output =', pv_has_malfunction(1, expected_data_normalized, measured_data_normalized))
    return

