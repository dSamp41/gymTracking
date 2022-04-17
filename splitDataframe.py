import pandas as pd
import numpy as np

def splitDf(df: pd.DataFrame) -> pd.DataFrame:
    '''
    DEF: Dataframe splittato è DF ma i pesi in array sono spacchettati.
         Riga, con array => 4 righe con peis singoli
    '''

    #Preparazione df splittato
    dfSplit = pd.DataFrame(columns=df.columns) #copia colonne
    dfSplit["date"] = np.repeat(df["date"], 4) #ripeti data 4 volte
    dfSplit.index = range(0, len(dfSplit.index))  #fix indici

    #Preparazione df delle medie
    dfAvg = pd.DataFrame()
    dfAvg["date"] = df["date"]


    esercizi = list(df.columns)
    esercizi.remove("date")

    for es in esercizi:
        dfAvg[f"{es}Average"] = df[es].map(lambda arr: np.mean(arr))  #operazione su df medie

        for index in range(0, len(dfSplit.index)):    #split su df
            dfSplit[es][index] = df[es][index//4][index%4]


    return dfSplit, dfAvg