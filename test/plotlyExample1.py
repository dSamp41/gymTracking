import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from Json2Dataframe import buildDataFrame



esercizi = ['squat', 'curl', 'extension', 'press', 'calfPress']
titleArray = []

df = buildDataFrame(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\jsonGambeExample1.jsonc")  #df con array di pesi separati
dfAvg = buildDataFrame(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc")

for es in esercizi: #aggiunge campo media in df con array uniti
    avgs = [np.mean(arr) for arr in dfAvg[es]]
    dfAvg[f"{es}Average"] = dfAvg[es].map(lambda arr: np.mean(arr))

    titleArray.append(f"Pesi {es}") 
    titleArray.append(f"Media {es}")
    
print(dfAvg, dfAvg.columns)


#PLOTTING
fig = make_subplots(rows=len(esercizi), cols=2, subplot_titles=titleArray)
colorScale = px.colors.qualitative.Plotly

for es in esercizi:
    index = esercizi.index(es) + 1
    
    fig.add_trace(go.Box(x=df["date"], y=df[es], name=f"distr {es}"), 
        row=index, col=1)
    fig.add_trace(go.Scatter(x=dfAvg["date"], y=dfAvg[f"{es}Average"], name=f"avg {es}"), 
        row=index, col=2)

fig.show()