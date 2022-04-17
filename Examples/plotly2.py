import plotly.express as px
from Json2Dataframe import buildDataFrame
import pandas as pd
import plotly.graph_objects as go
import numpy as np


df = px.data.tips()
#print(df)
#fig = px.strip(df, x="total_bill", y="day")

df1 = buildDataFrame(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc")
#print(df1)
#fig = px.strip(df1[0], x="date", y="squat")#, points="all")

dates = np.array(["2022-02-22", "2022-03-02", "2022-03-09", "2022-03-16", "2022-03-23"])
rep = np.array([0,1,2,3])
weights = np.array([[18, 20, 22, 22], [20, 20, 20, 20], [20, 20, 21, 21], [20, 21, 22, 23]])


#fig = px.strip(x=rep, y=weights)#, points="all")
#fig.show()

#fig = px.strip(df, x="time", y="total_bill", color="sex")
#fig.show()

s1 = pd.DataFrame(zip(dates, weights), columns=["date", "weights"])
fig = px.strip(s1, x='date', y=[18, 20, 22, 22])
fig.show()
print(s1)