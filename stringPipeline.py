# String to JSON Object
import json

def txt2Obj(s: str) -> dict :
    '''Data stringa in input [formato note], restituisce un dizionario formattato in schema JSON'''

    s = s.lower().replace("gambe", "date").replace("petto", "date").replace("dorso", "date")  #rimuove parte del corpo e inserisce date
    s = s.replace("calf press", "calfPress")
    s = s.replace("panca piana", "pancaPiana")
    s = s.replace("shoulder press", "shoulderPress")
    s = s.replace("back pack", "backPack")
    s = s.replace("alzate laterali", "alzateLaterali").split() #rimuove spazi


    #Formatta data
    s[1] = s[1].split("/") 
    s[1] = [int(s[1][i]) for i in range(0,3)]
    s[1].reverse()

    #Converte pesi in array
    for i in range(3, len(s), 2):
        s[i] = s[i].split("/")
        for j in range(0,4):
            s[i][j] = int(s[i][j])
      
    #Inserisce in dizionario
    dict = {}
    for i in range(0, len(s), 2):
        dict.update({s[i]: s[i+1]})
    
    return dict


def dictSort(dictList: list, key:str) -> dict:
    '''Dato array di dizionari, riordinarlo in-place secondo key crescente'''

    #insertion sort
    for i in range(0, len(dictList)-1):
        for j in range(i+1, len(dictList)):
            if(dictList[i][key] > dictList[j][key]):
                '''tmp = dictList[i][key]
                dictList[i][key] = dictList[j][key]
                dictList[j][key] = tmp'''

                tmp = dictList[i]
                dictList[i] = dictList[j]
                dictList[j] = tmp
    
    return dictList


#Inserire in obj in file json
def updateJson(path, newData: dict):
    '''
    Ricostruisce il file json, aggiungendo i nuovi dati

    Parameters
    --------
    path: (path-like) indirizzo del file json contenente i precedenti dati
    newData: dizionario contenente tracking di una certa data

    '''
    
    with open(path, "r") as file:
        tracking: dict = json.load(file)


    #Aggiorna array tracking con dati in input
    tracking["tracking"].append(newData)
    
    #Ridordina tracking per data crescente
    tracking["tracking"] = dictSort(tracking["tracking"], "date")


    #Ricostruisce file json
    with open(path, "w") as file:
        json.dump(tracking, file)


def stringPipeline(jsonPath, s: str):
    '''
    Pipeline: 
        · Converte stringa in dict\n
        · Aggiorna file json aggiungendo nuovo dict    
    '''
    
    updateJson(jsonPath, txt2Obj(s))
