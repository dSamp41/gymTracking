import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from Json2Dataframe import buildDataFrame

#fig = px.line(x=[1,2,3,4], y=[2,4,6,8], title="Example")
#fig = make_subplots(rows=1, cols=2)

'''df = pd.DataFrame(dict(
    date=["2020-01-10", "2020-02-10", "2020-03-10", "2020-04-10"],
    value=[[20,20,21,21], [21,21,21,21], [21,21,22,22], [22,22,22,23]],
))'''



#avgs = [np.mean(arr) for arr in df["value"]]

'''fig.add_trace(px.Scatter(x=df["date"], y=df["value"]))
fig.add_trace(go.Line(x=df["date"], y=avgs), row=1, col=2)
'''

eserc = "squat"

df = buildDataFrame(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc")
#df1 = df[["date", eserc]]

'''df2 = pd.DataFrame(data=[
    ["2022-02-22", "2022-03-02", "2022-03-09", "2022-03-16", "2022-03-23"], 
    [[18, 20, 22, 22], [20, 20, 20, 20], [20, 20, 21, 21], [20, 21, 22, 23], [20, 21, 22, 23]]
])'''


df2 = pd.DataFrame(data=[
    ["2022-02-22", [18, 20, 22, 22]], 
    ["2022-03-02", [20, 20, 20, 20]], 
    ["2022-03-09", [20, 20, 21, 21]],
    ["2022-03-16", [20, 21, 22, 23]],
    ["2022-03-23", [20, 21, 22, 23]],
    ["2022-03-25", [22, 23, 23, 24]]
], columns=["date", eserc])


dates = ["2022-02-22", "2022-03-02", "2022-03-09", "2022-03-16"]
rep = [1,2,3,4]
weights = [[18, 20, 20, 21], [20, 20, 21, 21], [20, 20, 21, 22], [21, 22, 22, 23]]
avgs = list(np.mean(arr) for arr in weights)

#df = pd.DataFrame(zip(rep,dates,weights), columns=["num","date","peso"])
#print(df[0])

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Box(x=dates, y=weights))
fig.add_trace(px.scatter(x=dates, y=avgs), row=1, col=2)

#fig = px.line(x=dates, y=avgs, markers=True)
fig.show()




#fig = px.box(x=dates, y=weights) #px.box(x=rep, y=weights, points="all")

