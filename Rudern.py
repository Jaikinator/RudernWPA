import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_names = ["aX","aY","aZ","temp","gX", "gY", "gZ"]

data = np.genfromtxt("Testmessung1.txt")
Dataframe = pd.read_table("Testmessung1.txt", delim_whitespace = True, header=None ,usecols= [2,6,10,14,18,22,26],names= col_names)
print(Dataframe)
print(Dataframe.columns.values)

plt.plot(Dataframe["aX"], Dataframe["aY"])
plt.show()