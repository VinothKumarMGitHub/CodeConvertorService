
import xml.etree.cElementTree as e
from types import SimpleNamespace

def ConvertToXMLLocal( root, propertyName,  obj ):
    if type(obj) is SimpleNamespace:
        xmlNode = e.SubElement(root, propertyName)  if propertyName != "root" else root    
        for attr, value in vars(obj).items():
            ConvertToXMLLocal(xmlNode, attr, value)
    elif type(obj) is list:
        xmlNode = e.SubElement(root, propertyName)  
        for item in obj: 
            ConvertToXMLLocal( xmlNode, propertyName, item)
    else:
        e.SubElement( root, propertyName).text = str(obj)

def ConvertToXML(obj):
    xmlRoot = e.Element("root")
    ConvertToXMLLocal( xmlRoot, "root", obj )
    e.ElementTree( xmlRoot)
    return e.tostring(xmlRoot)
    