import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("../dataset/finaltipteldataset.csv",on_bad_lines='skip')

totaldias = np.arange(1,32)

days = data['FECHA DE VENTA']
#unique days
unique_days=days.drop_duplicates()

composed_days=[]

for i,row in unique_days.items():
    light = data['FECHA DE VENTA']==row
    final = data[light].shape
    composed_days.append([row,final[0]])
np_composed_days = np.array(composed_days)
pre_number_data = np_composed_days[:,1]
number_data = pre_number_data.astype(np.int32)

ax = plt.subplot()
ax.tick_params(axis='x',labelrotation=90)

newara = np.array(number_data)
newar = newara[31:31+28+3]
newar[-1]=0
newar[-2]=0
newar[-3]=0

plt.plot(totaldias,number_data[:31],label="Enero")
plt.plot(totaldias,newar,label="Febrero")
plt.plot(totaldias,number_data[31+28:],label="Marzo")
plt.legend()
plt.show()

# dataFrame = pd.DataFrame(np_composed_days,columns=['fecha','cantidad'])

# pd.set_option('display.max_rows', dataFrame.shape[0]+1)

# print(dataFrame[59:])
