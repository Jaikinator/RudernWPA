import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_names = ["aX","aY","aZ","temp","gX", "gY", "gZ"]  # festlegen welche Daten importiert werden

Dataframe = pd.read_excel("RUDERN_Messung.xlsx")#einlesen der Daten

#def get_dataset(arduino,Messung):


#time_sim = np.arange(0, (len(Dataframe["aX"]))) # zeitsimulation


print(Dataframe[Dataframe["AccX [g]"] == "Pause"].index.values) # print der Daten
print(Dataframe.columns.values) # Print der Spaltennamen
Dataframe_copy = Dataframe.copy().drop([:])
print(Dataframe_copy)
#velocitiy_x = np.trapz(Dataframe["aX"].to_numpy())
# Grafische Darstellung der Daten
#print(velocitiy_x )
#plt.plot(time_sim,velocitiy_x)
#plt.show()
'''
plt.subplot(211)
plt.plot(time_sim, Dataframe["gX"], label = "gyro X")
plt.plot(time_sim, Dataframe["gY"], label = "gyro Y")
plt.plot(time_sim, Dataframe["gZ"], label = "gyro Z")
plt.legend()

plt.subplot(212)
plt.plot(time_sim, Dataframe["aX"], label = "acc X")
plt.plot(time_sim, Dataframe["aY"], label = "acc Y")
plt.plot(time_sim, Dataframe["aZ"], label = "acc Z")
plt.legend()
plt.show()
'''