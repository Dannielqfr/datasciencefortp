import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("../dataset/finaltipteldataset.csv",on_bad_lines='skip')

def valuelabel(x_axis,y_axis):
    for i in range(len(x_axis)):
        plt.text(i,y_axis[i],y_axis[i], ha = 'center',
                 bbox = dict(facecolor = 'cyan', alpha =0.8))

days = data['FECHA DE VENTA']
#unique days
unique_days=days.drop_duplicates()

composed_days=[]

for i,row in unique_days.items():
    light = data['FECHA DE VENTA']==row
    final = data[light].shape
    composed_days.append([row,final[0]])
    #print(final[0])
np_composed_days = np.array(composed_days)
pre_number_data = np_composed_days[:,1]
number_data = pre_number_data.astype(np.int32)

valuelabel(np_composed_days[59:,0],number_data[59:])
ax = plt.subplot()
ax.tick_params(axis='x',labelrotation=90)

plt.plot(np_composed_days[59:,0],number_data[59:])
plt.show()