
from dateutil.parser import parse
from types import SimpleNamespace

class CSharp:
    def __init__(self, name) -> None:
        self.name = self.getClassName( name )
        self.properties = []

    def addProperty(self, propertyName, value, objectType ):
        self.properties.append( ( self.camelCase( propertyName ), self.resolveType(objectType, value, self.getClassName( propertyName))  ) )

    def __str__(self) -> str:
        strVal =  "public class " + self.name + "\n"
        strVal = strVal + "{" + "\n"
        
        for prop in self.properties:
            name, objType = prop
            strVal = strVal +  "\tpublic " + objType + " " + name  + "{ get; set; }\n"

        strVal = strVal + "}" + "\n"
        return strVal

    def getClassName(self, value):
        retValue =  value[0].upper() +  value[1: len(value)-1 ] + ( "" if value[-1].lower() == "s" else value[-1]  )
        return retValue

    def pascelCase(self, value):
        retValue =  value[0].upper() +  value[1:len(value)]  
        return retValue

    def camelCase(self, value):
        retValue =  value[0].lower() +  value[1:len(value)]  
        return retValue

    def is_date(self, string, fuzzy=False):
        """
        Return whether the string can be interpreted as a date.

        :param string: str, string to check for date
        :param fuzzy: bool, ignore unknown tokens in string if True
        """
        try: 
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False

    def resolveType(self, objectType,value, propertyName):
        
        strType = objectType.__name__
        if objectType.__name__ == "list":
            strType = "List<" + propertyName + ">"
        elif objectType.__name__ == "set":
            strType = "HashSet<" + propertyName + ">"
        elif objectType.__name__ == "str":
            strType = "string"
            if value != None and self.is_date(value):
                strType = "DateTime" 
        return strType


def ConvertToCSharp( root, propertyName,  obj , classList ):

    if type(obj) is SimpleNamespace:
        cSharpObj = CSharp(propertyName)
        if root != None:
            root.addProperty(  propertyName, obj,  type(obj) )
        for attr, value in vars(obj).items():
            ConvertToCSharp(cSharpObj, attr, value, classList)
        classList.append(cSharpObj)
    elif type(obj) is list:
        if len(obj) > 0:
            if type( obj[0]) is SimpleNamespace:
                ConvertToCSharp( None, propertyName, obj[0], classList)
            root.addProperty( propertyName, None,  type(obj) )    
        else:
            root.addProperty(  propertyName, None, list ) 
    else:
        root.addProperty(  propertyName, obj,  type(obj) )

    return True
