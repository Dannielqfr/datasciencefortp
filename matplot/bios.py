import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def valuelabel(x_axis,y_axis):
    for i in range(len(x_axis)):
        plt.text(i,y_axis[i],y_axis[i], ha = 'center',
                 bbox = dict(facecolor = 'cyan', alpha =0.8))

data = pd.read_csv("../dataset/finaltipteldataset.csv",on_bad_lines='skip')

data['RAZON SOCIAL LECTOR']=data['RAZON SOCIAL LECTOR'].replace({'MEGA CONNECTION S.A.C.':'MEGA'},regex=True)
data['RAZON SOCIAL LECTOR']=data['RAZON SOCIAL LECTOR'].replace({'SERVICIO DE TELECOMUNICACIONES MEGA':'MEGA'},regex=True)

is_mega = data['RAZON SOCIAL LECTOR']=='MEGA'
biometricos = data['SERIE LECTOR'][is_mega]
unique_biometricos=biometricos.drop_duplicates()
composed_bios=[]

for i,row in unique_biometricos.items():
    light_bio = data['SERIE LECTOR']==row
    final_bio = data[light_bio].shape
    composed_bios.append([row,final_bio[0]])
np_composed_bios = np.array(composed_bios)
pre_bio_data = np_composed_bios[:,1]
number_data_bio = pre_bio_data.astype(np.int32)

ax = plt.subplot()
ax.tick_params(axis='x',labelrotation=90)
valuelabel(np_composed_bios[:,0],number_data_bio)

plt.bar(np_composed_bios[:,0],number_data_bio)
plt.show()