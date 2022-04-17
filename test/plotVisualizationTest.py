from plotly.subplots import make_subplots
import plotly.graph_objects as go

from splitDataframe import splitDf
from Json2Dataframe import buildDataFrame


path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc"
df = buildDataFrame(path)

dfSplit, dfAvg = splitDf(df)
eserc = "squat"

fig = make_subplots(rows=1, cols=2, subplot_titles=eserc)
    
fig.add_trace(go.Box(x=dfSplit["date"], y=dfSplit[eserc], name=f"distr {eserc}"), row=1, col=1)
fig.add_trace(go.Scatter(x=dfAvg["date"], y=dfAvg[f"{eserc}Average"], name=f"avg {eserc}"), row=1, col=2)

fig.show()