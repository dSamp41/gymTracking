from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas as pd
from splitDataframe import splitDf
from Json2Dataframe import buildDataFrame


path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc"
df = buildDataFrame(path)

dfSplit, dfAvg = splitDf(df)
esercizi = list(dfSplit.columns)
esercizi.remove("date")

eserc = "squat"
fig = make_subplots(rows=1, cols=2, subplot_titles=eserc)


app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Gym Tracker'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    #dcc.Dropdown(options=["Dorso", "Gambe", "Petto"], value="Dorso", id="bodyPart"),
    dcc.Dropdown(options=esercizi, value="squat", id="esercName"),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output(component_id='example-graph', component_property="figure"),
    Input(component_id='esercName', component_property="value"),
    #Input(component_id='bodyPart', component_property="value")
)
def update_graph(esercName):
    fig = make_subplots(rows=1, cols=2)
    
    fig.add_trace(go.Box(x=dfSplit["date"], y=dfSplit[esercName], name=f"distr {esercName}"), row=1, col=1)
    fig.add_trace(go.Scatter(x=dfAvg["date"], y=dfAvg[f"{esercName}Average"], name=f"avg {esercName}"), row=1, col=2)

    return fig



if __name__ == '__main__':
    app.run_server()