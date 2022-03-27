# String to JSON Object
import json
from xxlimited import new

def txt2Obj(s: str) -> dict :
    '''Data stringa in input [formato note], restituisce un dizionario formattato in schema JSON'''

    s = s.lower().replace("gambe", "date").replace("petto", "date").replace("dorso", "date")  #rimuove parte del corpo e inserisce date
    s = s.replace("calf press", "calfPress").split() #rimuove spazi

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
