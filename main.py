from stringPipeline import stringPipeline
#import stringPipeline
from plotUtil import buildGraph
from Json2Dataframe import buildDataFrame

'''
Aggiungere nuovo oggetto tracking?
    y: string pipeline -> buildDataframe
    n: input str esercizio -> buildGraph
'''

def main(path):
    answer = input("Inserire nuovo tracking? [y/n]")
    if(answer == "y"):
        s = str(input("Inserisci sessione di allenamento: ")).toLower()
        stringPipeline.stringPipeline(path, s)

    elif(answer == "n"):
        eserc = str(input("Inserisci esercizio da visualizzare: "))
        buildGraph(buildDataFrame(path), eserc)

    else:
        print("RIP")


if(__name__=="__main__"):
    path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\jsonGambeExample.jsonc"
    main(path)