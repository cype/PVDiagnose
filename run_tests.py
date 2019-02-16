from test_statdiagnostics import test_statdiagnostics
from productiondata import *

#martins PV
print('martins PV')

area = 45
peak_power = 5.6
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
'''
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
'''
measured_data = [
    0,
    55,
    89,
    300,
    646,
    565,
    699,
    692,
    540,
    582,
    259,
    122
]

months = [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
#months = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

test_statdiagnostics(area, peak_power, expected_data, measured_data, months)

#obersunne alersheim
print('\nobersunne alersheim PV')

area = 114 * 1.634 * 0.986
peak_power = 29.64
expected_data = [
    3.740368649,
    2.7041781425,
    4.4793855014,
    10.7333747141,
    17.4047102942,
    22.4823071366,
    27.3034660366,
    26.3150983053,
    20.3594458257,
    20.6484686166,
    9.4704325324,
    5.4501307449
]
measured_data = [
    530.88,
    436.91,
    725.69,
    1610,
    2650,
    3430,
    4140,
    4100,
    3310,
    3300,
    1460,
    910.47
]
months = [1, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

test_statdiagnostics(area, peak_power, expected_data, measured_data, months)

# uberlandstrasse
print('\nÜberlandstrasse PV')
peak_power = 10.44
test_statdiagnostics(Uberlandstrasse_size, peak_power, Uberlandstrasse2d_erwartung, Uberlandstrasse2d_2018, months)

# batastrasse
print('\nBatastrasse PV')
peak_power = 29.92
test_statdiagnostics(Batastrasse_size, peak_power, Batastrasse40_erwartung, Batastrasse40_2018, months)

#Turnhalle Gerenmatte
print('\ngerenmatte turnhalle PV')

area = 209.4
peak_power = 29.9
expected_data = [
    3.678451416,
    5.535455476,
    9.531722907,
    20.74223832,
    20.38633695,
    26.47510769,
    27.45891763,
    22.49533782,
    17.59258905,
    10.73653655,
    4.536044433,
    2.706053459
]
measured_data = [
    652.33,
    642.95,
    1720,
    4100,
    4160,
    5170,
    4870,
    3810,
    2950,
    1810,
    811.1,
    493.96
]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

test_statdiagnostics(area, peak_power, expected_data, measured_data, months)
