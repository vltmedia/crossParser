"""
Author: Justin Jaro
License: MIT
Description:
Parse a python argparse object into CSharp, Javascript, and Python classes.
This is useful for creating a GUI for a python script.
"""

import argparse 

def parserToJSON(parser, className = "Options"):
    outputJSON = {"className": className, "options": []}
    classes = []
    for item in parser._actions:
        if isinstance(item, argparse._StoreAction):
            defaultVal = ""
            help_ = ""
            
            typeText = "string"
            if item.type == bool:
                if item.default:
                    defaultVal = "true"
                else:
                    defaultVal = "false"
                typeText = "bool"
            elif item.type == int:
                defaultVal = item.default
                
                if defaultVal == "inf" or defaultVal == float("inf"):
                    defaultVal = "99999"
                typeText = "int"
            elif item.type == float:
                defaultVal = item.default or defaultVal == float("inf")
                if defaultVal == "inf":
                    defaultVal = "99999"
                typeText = "float"
            elif item.type == str:
                defaultVal = f"\"{item.default}\""
                typeText = "string"
            if item.help != None:
                help_ = f"\"{item.help}\""
            required = False
            try:
                required = item.required
            except:
                v = 0
            try:
                if item.action == "store_true":
                    defaultVal = "false"
                    typeText = "bool"
                if item.action == "store_false":
                    defaultVal = "true"
                    typeText = "bool"
            except:
                v = 0
            outputJSON["options"].append({"name": item.dest, "type": typeText, "default": defaultVal, "required": required, "help": help_})
    return outputJSON


def parserToCSharpClass(parser, className = "Options"):
    classes = ["public class "+className+" {", "", ""]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        outText = f"public {item['type']} {item['name'].replace(' ', '_')} = {item['default']};"
        classes.append(outText)
    classes.append("")  
    classes.append("")  
    classes.append("// -------------- Help --------------")  
    classes.append("")  
        # //
    for item in optionsJson["options"]:
        if item['help'] != ""and item['help'] != None:
            outText = f"public string {item['name'].replace(' ', '_')}_Help = {item['help']};"
            classes.append(outText)
    classes.append("")  
    classes.append("")  
    classes.append("}")  
    outData = "\n".join(classes)
    return outData


def parserToJavascriptClass(parser, className = "Options"):
    classes = ["export class "+className+" {", "", "", "constructor() {"]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        outText = f"this.{item['name'].replace(' ', '_')} = {item['default']};"
        classes.append(outText)  
    classes.append("")  
    classes.append("")  
    classes.append("// -------------- Help --------------")  
    
    classes.append("")  
        
    for item in optionsJson["options"]:
        if item['help'] != ""and item['help'] != None:
            outText = f"this.{item['name'].replace(' ', '_')}_Help = {item['help']};"
            classes.append(outText)
    classes.append("")  
    classes.append("")  
    classes.append("}")  
    classes.append("")  
    classes.append("")  
    classes.append("}")  
                
    outData = "\n".join(classes)
    return outData


def parserToPythonClass(parser, className = "Options"):
    classes = ["class "+className+":", "", "", "    def __init__(self):"]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        devaultVal = item['default']
        if item['default'] == "true":
            devaultVal = "True"
        if item['default'] == "false":
            devaultVal = "False"
        outText = f"        self.{item['name'].replace(' ', '_')} = {devaultVal }"
        classes.append(outText)  
    classes.append("")  
    classes.append("")  
    classes.append("# -------------- Help --------------")  
    
    classes.append("")  
        
    for item in optionsJson["options"]:
        if item['help'] != "" and item['help'] != None:
            outText = f"        self.{item['name'].replace(' ', '_')}_Help = {item['help']}"
            classes.append(outText)
    classes.append("")  
                
    outData = "\n".join(classes)
    return outData



