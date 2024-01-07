import pandas as pd
import json
import datetime


def buildDataFrame(path):
    '''
    Costruisce dataframe a partire da dati contenuti nel file JSON in path
    '''

    with open(path, "r") as read_file:
        dataFromJSON = json.load(read_file)

    dataFrame = pd.DataFrame(data=dataFromJSON["tracking"])
    dataFrame["date"] = dataFrame["date"].map(lambda d : datetime.date(d[0], d[1], d[2]))   # Array -> Date

    #dataFrame.to_csv(r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\gymTracking.csv") #TODO: fix 
    return dataFrame



def splitDataFrame(df: pd.DataFrame, esercizi: list):
    '''
    Dato df completo, ritorna df composto da esercizi presenti in lista
    
    '''

    return df[esercizi].dropna()