from statdiagnostics import pv_has_malfunction
from matplotlib import pyplot as plt

import pandas as pd

#martins PV

area = 45
expected_data = [
    5.5790842527,
    2.9860944866,
    4.0484830468,
    12.5247770721,
    18.5556731463,
    21.9093255392,
    28.4363443623,
    26.3829326719,
    20.4131881961,
    22.5740697919,
    11.0800516792,
    5.9010270749]
measured_data = [
    87.7,
    47.6,
    103,
    329,
    392,
    564,
    699,
    692,
    540,
    582,
    258,
    122
]

months = [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

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

'''
plt.bar(months, expected_data, align='center')
plt.show()

plt.bar(months, measured_data, align='center')
plt.show()
'''

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
    'reference normalized' : expected_data_normalized,
    'measured normalized' : measured_data_normalized
    },index = months
)
df_rearanged.plot(kind='bar')
plt.show()

print('normalized data + perturbation: output =', pv_has_malfunction(1, expected_data_normalized, measured_data_normalized))
