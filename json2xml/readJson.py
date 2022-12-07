
import json
from types import SimpleNamespace

#function reads json file
def paserJsonString(jsonString):
    return json.loads(jsonString, object_hook=lambda d: SimpleNamespace(**d))

#function reads json file
#return file content 
def readJsonFromFile(fileName):
    #read json file content
    with open(fileName) as fh:
        return  fh.read()
    #return nothing 
    return ""

#function reads json file
#return file content 
def readJsonFromURL(url):
    #dounload file from server 
    fileContent =  url
    return fileContent
 
# jsonContent =  readJsonFromFile("sample.json")
# pythonObj = paserJsonString( jsonContent)
# cSharpClassList = []

# xmlString =  ConvertToXML( pythonObj)
# print(xmlString)

