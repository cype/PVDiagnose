import pandas as pd
import os

ddir = "/Users/brauliobarahonagarzon/Desktop/solar_dach"

# renewables ninja data from -> 2011 - 2014
# *! next step
#fns=["ninja_pv_47.4104_8.4088_2014.csv",
#"ninja_pv_47.4104_8.4088_2015.csv",
#"ninja_pv_47.4104_8.4088_2016.csv",
#"ninja_pv_47.4104_8.4088_2017.csv"]

# angelous ekz data and corresponding sonnendach data 
fn = 'sonnendach_data_locAngelous.json'
fnA = 'photovoltaic_1550238945139.csv'

with open(os.path.join(ddir,fn)) as json_data:
    d = json.load(json_data)
    #print(d)
#
#'heizgradtage'
#'gstrahlung'
monats_ertrag= d['results'][0]['attributes']['monats_ertrag']
months= d['results'][0]['attributes']['monate']

#
PVm=pd.read_csv(os.path.join(ddir,fnA), sep=';', header=0)
Whm2=PVm["Gesamt-Stromerzeugung Wh"]/53.35*1e-3

# Mock test 
#sigma=0.5
#userinp=sigma * np.random.randn(1000, 12) + monats_ertrag
#ix = np.random.randint(1,len(userinp))
#delta= Whm2 - monats_ertrag

bar(months, monats_ertrag, alpha=0.7, label='sonnendach')
bar(list(range(1,13)), Whm2, alpha=0.4, label='measured')
plt.title(str(np.round(np.sum(delta),4)))
plt.legend()
