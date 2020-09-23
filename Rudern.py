import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Dataframe = pd.read_excel("RUDERN_Messung.xlsx")#einlesen der Daten


def velocity(df):
    headers = df.columns.values

    accX = df[headers[0]].to_numpy()
    accY = df[headers[1]].to_numpy()
    accZ = df[headers[2]].to_numpy()
    time = df["time [s]"].to_numpy()

    velocity_x = np.zeros(len(accX))
    velocity_y = np.zeros(len(accY))
    velocity_z = np.zeros(len(accZ))

    for i in range(len(accX)):

        velocity_x[i] = np.trapz(accX[i-1 : i+1], x =  time[i-1 : i+1])
        velocity_y[i] = np.trapz(accY[i-1 : i+1], x =  time[i-1 : i+1])
        velocity_z[i] = np.trapz(accZ[i-1 : i+1], x =  time[i-1 : i+1])
        print(accX[i-1 : i+1 ])
    df.insert(7, "v_X [m/s^2]", velocity_x)
    df.insert(8, "v_Y [m/s^2]", velocity_y)
    df.insert(9, "v_Z [m/s^2]", velocity_z)

    return df

def get_dataset(arduino, Messung, df = Dataframe):

    Dataframe = df.dropna(subset=["AccX [g]"]).reset_index(drop= True)

    headers = df.columns.values  # Print der Spaltennamen

    pause_array = Dataframe[Dataframe["AccX [g]"] == "Pause"].index.values #Array mit Pausen stellen

    select_measure = Dataframe[pause_array[Messung]+1: pause_array[Messung+1]].reset_index(drop = True)

    output_frame = pd.DataFrame(columns = headers)


    i = 0
    while i < len(select_measure):
         output_frame = output_frame.append(select_measure.loc[arduino+i], ignore_index= True)
         i += 3

    output_frame["AccX [g]"] = output_frame["AccX [g]"].astype(float)

    output_frame = velocity(output_frame)
    return output_frame

dataset_1 = get_dataset(0,1)

time_set = dataset_1["time [s]"].to_numpy()

headers = dataset_1.columns.values

print(dataset_1)


plt.plot(time_set, dataset_1[headers[-2]], label = "VX")
plt.plot(time_set, dataset_1[headers[0]], label = "accX")

plt.plot(time_set, dataset_1[headers[1]], label = "acc Y")
plt.plot(time_set, dataset_1[headers[2]], label = "acc Z")
plt.legend()

plt.show()
