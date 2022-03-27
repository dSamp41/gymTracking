import json
from os import PathLike

path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc"
ee = {'date': [2022, 4, 10], 'squat': [180, 200, 20, 220], 'curl': [45, 450, 450, 45], 'extension': [40, 400, 450, 45], 'press': [110, 1010, 1010, 120], 'calfPress': [150, 1500, 1050, 1500]}

def updateJson(path: PathLike, newData: dict):
    '''
    Ricostruisce il file json,aggiungendo i nuovi dati

    Parameters
    --------
    path: (path-like) indirizzo del file json contenente i precedenti dati
    newData: (dict) dizionario contenente dati di una certa data

    '''
    with open(path, "r") as file:
        tracking = json.load(file)


    #Aggiorna array tracking con dati in input
    tracking["tracking"].append(newData)


    #Ricostruisce file json
    with open(path, "w") as file:
        json.dump(tracking, file)

#updateJson(path, ee)

