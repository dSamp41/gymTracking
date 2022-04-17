from stringPipeline import *

tr = """Petto 18/02/2022
panca piana 20/20/20/20
spinte 16/16/18/18
shoulder press 40/42/42/42
back pack 30/30/35/35
alzate laterali 0/0/0/0"""

def readFromFile(filePath, jsonPath):
    with open(filePath) as file:
        trackData = file.read()
    
    updateJson(jsonPath, txt2Obj(trackData))
    

filePath = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\petto.txt"
path = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\testPettoPacked.jsonc"

readFromFile(filePath, path)
print("COMPLETED")