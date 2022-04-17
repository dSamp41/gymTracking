from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from splitDataframe import splitDf
from Json2Dataframe import buildDataFrame


def viewTracking():
    pathDict = {"Gambe": r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\testGambePacked.jsonc",
        "Petto": r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\testPettoPacked.jsonc",
    }

    path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\testGambePacked.jsonc"


    fig = make_subplots(rows=1, cols=2)

    esercDict = {"Gambe": ['squat', 'curl', 'extension', 'press', 'calfPress'], 
             "Petto": ['pancaPiana', 'spinte', 'shoulderPress', 'backPack', 'alzateLaterali'],
             "Dorso": []
    }

    bodyPartList = list(esercDict.keys())
    esercOptions = esercDict[bodyPartList[0]]


    app = Dash(__name__)
    app.layout = html.Div(children=[
        html.H1(children='Gym Tracker'),
        html.Div(children='''Dash: A web application framework for your data. w\ func'''),
        dcc.Dropdown(
            id ="bodyPart",
            options = [{"label": name, "value": name} for name in bodyPartList], 
            value = "Gambe"
            ), 
        dcc.Dropdown(id="esercName", value="squat"),
        html.H3(children="squat", id="esercTitle"),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])


    @app.callback(
    Output(component_id="esercName", component_property="options"),
    Input(component_id="bodyPart", component_property="value")
    )
    def updateEsercOptDropdown(bodyPart):
        '''Aggiorna le opzioni del secondo menù dropdown, restituendo gli esercizi legata alla parte scelta'''
        return [{"label": eserc, "value": eserc} for eserc in esercDict[bodyPart]]



    @app.callback(
    Output(component_id='esercTitle', component_property="children"),
    Input(component_id='esercName', component_property="value"),
    )
    def update_title(esercName):
        return esercName


    @app.callback(
    Output(component_id='example-graph', component_property="figure"),
    Input(component_id='esercName', component_property="value"),
    Input(component_id="bodyPart", component_property="value")
    )
    def update_graph(esercName, bodyPart):
        df = buildDataFrame(pathDict[bodyPart])
        dfSplit, dfAvg = splitDf(df)
    
        fig = make_subplots(rows=1, cols=2)
    
        fig.add_trace(go.Box(x=dfSplit["date"], y=dfSplit[esercName], name=f"distr {esercName}"), row=1, col=1)
        fig.add_trace(go.Scatter(x=dfAvg["date"], y=dfAvg[f"{esercName}Average"], name=f"avg {esercName}"), row=1, col=2)

        return fig


    #if __name__ == '__main__':
    app.run_server()
