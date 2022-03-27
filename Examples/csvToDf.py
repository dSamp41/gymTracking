import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\gymTracking.csv")
#df["squat"].map(lambda a: np.array(a))
print(df["squat"].dtypes)


df1 = pd.read_json(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc")
print(df1[0])

'''
plt.boxplot(df["squat"])
plt.show()
'''