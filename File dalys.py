import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/submerge/IBI1_2023-24")
print(os.getcwd())
dalys_data = pd.read_csv("Practical7/dalys-rate-from-all-causes(1).csv")
# Changed the current working directory to the specified folder, read the files in the folder, and save them in variables.

print(dalys_data.head())
subset = dalys_data.iloc[0:100:10, 3]
print("Selected subset:")
print(subset)
filtered_data = dalys_data[dalys_data.loc[:,"Entity"]=="Afghanistan"]
print("Data for Afghanistan:")
print(filtered_data.iloc[:,3])
compare_years = ["2019"]
yearly_daly_values = [v[2] for v in china_data[compare_years].values()]
mean_all = np.mean(china_data['DALYs'].astype(float))
mean_2019 = np.mean(yearly_daly_values)
if mean_2019 > mean_all:
    print("2019 had a higher mean DALYs")
elif mean_2019 < mean_all:
    print("2019 had a lower mean DALYs")
else:
    print("The mean DALYs for 2019 was equal to the mean for all years")
# Use Boolean values to select data. Convert numbers to string format.

# We used the matplotlib library to draw data graphs of DALYs for China and the United Kingdom in different years
import matplotlib.pyplot as plt
plt.plot(china_data.Year, china_data.DALYs, 'b+', label='China')
plt.xticks(china_data.Year, rotation=-90)
plt.show()
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
plt.plot(uk_data.Year, uk_data.DALYs, label='United Kingdom')
plt.legend()
plt.show()
