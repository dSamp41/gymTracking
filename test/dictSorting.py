a = [{"key":4, "val":2}, {"key":1, "val":6}, {"key":3, "val":12}, {"key":5, "val":3}, {"key":2, "val":16}]


def dictSort(dictList: list, key:str) -> dict:
    '''Dato array di dict, riordinarlo in-place secondo key crescente'''

    #insertion sort
    for i in range(0, len(dictList)-1):
        for j in range(i+1, len(dictList)):
            if(dictList[i][key] > dictList[j][key]):
                tmp = dictList[i][key]
                dictList[i][key] = dictList[j][key]
                dictList[j][key] = tmp
    
    return dictList

import json
#Inserire in obj in file json
def updateJson(path, newData: dict):
    '''
    Ricostruisce il file json, aggiungendo i nuovi dati

    Parameters
    --------
    path: (path-like) indirizzo del file json contenente i precedenti dati
    newData: (dict) dizionario contenente dati di una certa data

    '''
    
    with open(path, "r") as file:
        tracking = json.load(file)


    #Aggiorna array tracking con dati in input
    tracking["tracking"].append(newData)
    tracking["tracking"] = dictSort(tracking["tracking"], "date")

    return tracking


    '''
    #Ricostruisce file json
    with open(path, "w") as file:
        json.dump(tracking, file)
        '''

path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc"
dt = {'date': [2022, 2, 12], 'squat': [15, 18, 20, 22,2], 'curl': [40, 40, 40, 40], 'extension': [35, 35, 40, 40], 'press': [100, 100, 110, 120], 'calfPress': [140, 140, 140, 140]}
print(updateJson(path, dt))

