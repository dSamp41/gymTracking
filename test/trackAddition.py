from stringPipeline import *

def readFromFile(filePath, jsonPath):
    with open(filePath) as file:
        trackData = file.read()
    
    updateJson(jsonPath, txt2Obj(trackData))
    


txtPath = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\petto.txt"
jsonPath = r"C:\Users\Daniele\Desktop\Programmazione\Python\gymTracking\test\testPettoPacked.jsonc"

readFromFile(txtPath, jsonPath)
print("COMPLETED")
