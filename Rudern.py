import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_names = ["aX","aY","aZ","temp","gX", "gY", "gZ"]  # festlegen welche Daten importiert werden

Dataframe = pd.read_excel("RUDERN_Messung.xlsx")#einlesen der Daten


headers = Dataframe.columns.values

def get_dataset(arduino = 1 ,Messung = 0,df = Dataframe):

    Dataframe = df.dropna(subset=["AccX [g]"]).reset_index(drop= True)

    headers = df.columns.values  # Print der Spaltennamen

    pause_array = Dataframe[Dataframe["AccX [g]"] == "Pause"].index.values #Array mit Pausen stellen

    select_measure =  Dataframe[pause_array[Messung]+1: pause_array[Messung+1]].reset_index(drop = True)

    output_frame = pd.DataFrame(columns = headers)


    i = 0
    while i < len(select_measure):
         output_frame = output_frame.append(select_measure.loc[arduino+i], ignore_index= True)
         i += 3

    return output_frame

print(get_dataset())

"""
newframe = pd.DataFrame(columns = headers )

print(newframe.append(Dataframe.loc[2])) #appand dataframe
#time_sim = np.arange(0, (len(Dataframe["aX"]))) # zeitsimulation
Dataframe["index1"] = Dataframe.index

testframe = Dataframe.dropna(subset=["AccX [g]"])
print( testframe[testframe["AccX [g]"] == "Pause"].index.values) # print der Daten
print(Dataframe.columns.values) # Print der Spaltennamen
"""
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