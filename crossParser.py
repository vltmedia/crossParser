"""
Author: Justin Jaro
License: MIT
Description:
Parse a python argparse object into CSharp, Javascript, and Python classes.
This is useful for creating a GUI for a python script.
"""

import argparse 

def sanitizeText (text):
    return text.replace("\"", "\\\"")


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
                if defaultVal == None:
                    defaultVal = "0"
                typeText = "int"
            elif item.type == float:
                defaultVal = item.default or defaultVal == float("inf")
                if defaultVal == "inf":
                    defaultVal = "99999"
                if defaultVal == None:
                    defaultVal = "0"
                typeText = "float"
            elif item.type == str:
                defaultVal = f"\"{item.default}\""
                if item.default == None or item.default == "None":
                    defaultVal = "\"\""
                typeText = "string"
            if item.help != None:
                help_ = f"\"{sanitizeText(item.help)}\""
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



def generateUAIForm(parser, className = "ImageForm"):
    from parsers.uai import getLineEdit, getSpinbox, getDoubleSpinbox, getToggle, getDropDown
    classes = ["using System;",
"using System.Collections.Generic;",
"using System.Linq;",
"using System.Text;",
"using System.Threading.Tasks;",
"using TMPro;",
"using uai.ai;",
"using uai.common;",
"using uai.common.objects;",
"using uai.networking;",
"using uai.ui;",
"using UnityEngine;",
"using UnityEngine.UI;","","","namespace uai.runners.ai{",   "public class "+className+" : ImageRequestForm{", "", "" ]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        outText = ""
        if item['type'] == "float":
            item['default'] = str(item['default'])+"f"
            outText = getDoubleSpinbox(item['name'].replace(' ', '_'))
        if item['type'] == "int":
            outText = getSpinbox(item['name'].replace(' ', '_'))
        if item['type'] == "string" or  item['type'] == "str"   :
            outText = getLineEdit(item['name'].replace(' ', '_'))
        if item['type'] == "bool" :
            outText = getToggle(item['name'].replace(' ', '_'))
        classes.append(outText)
    classes.append("""
            void Start()
        {
            runnerType = RunnerType.Python;
            onOpenFile.AddListener(OnImportImage);
        }

        private void OnImportImage(bool arg0, string filepath)
        {
        
            GameState.ShowMediaFilepath(filepath);
        }

""")
    classes.append("""
        public override void SetRequest()
        {
            base.SetRequest();
""")
    classes.append(f"runner.SetModulePath(\"{className}\");")
    classes.append("""

            request.input = Convert.ToBase64String(File.ReadAllBytes(loadedPath));
            request.submode = "base64";
            request.mode = "all";
        }
        public override void Finished()
        {
            result = JsonUtility.FromJson<MultipleMediaRequest>(recievedStringData);
            mediaCatalog.AddPack(result);
            GameState.SetResultType("MultipleMediaRequest.Base64");
            base.Finished();
        }
                """)  
    classes.append("")  
    classes.append("")  
    classes.append("}") 
    classes.append("")  
     
    classes.append("}")  
    outData = "\n".join(classes)
    return outData
        

def generateUnityForm(parser, className = "ImageForm"):
    from parsers.uai import getTMP_InputField, getToggle, getDropDown
    classes = ["using System;",
"using System.Collections.Generic;",
"using System.Text;",
"using TMPro;",
"using UnityEngine;",
"using UnityEngine.UI;", "","","public class "+className+" : MonoBehaviour{", "", ""]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        outText = getTMP_InputField(item['name'].replace(' ', '_'))
        if item['type'] == "float":
            item['default'] = str(item['default'])+"f"
            outText = getTMP_InputField(item['name'].replace(' ', '_'))
        if item['type'] == "int":
            outText = getTMP_InputField(item['name'].replace(' ', '_'))
        if item['type'] == "string" or  item['type'] == "str"   :
            outText = getTMP_InputField(item['name'].replace(' ', '_'))
        if item['type'] == "bool" :
            outText = getToggle(item['name'].replace(' ', '_'))
        classes.append(outText)
    classes.append("")  
    classes.append("")  
    classes.append("}")  
    outData = "\n".join(classes)
    return outData
        
        
def parserToCSharpClass(parser, className = "Options"):
    classes = ["public class "+className+" {", "", ""]
    optionsJson = parserToJSON(parser, className)
    for item in optionsJson["options"]:
        if item['type'] == "float":
            item['default'] = str(item['default'])+"f"
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


def parserToHTMLForm(parser, className = "Options"):
    from parsers.html import generateHTMLForm
    optionsJson = parserToJSON(parser, className)
    return generateHTMLForm(className, optionsJson['options'])


def parserToHTMLFormPage(parser, className = "Options"):
    from parsers.html import generateHTMLFormPage
    optionsJson = parserToJSON(parser, className)
    return generateHTMLFormPage(className, optionsJson['options'])



def parserToReactTailwindMaterialComponent(parser, className = "Options"):
    from parsers.react import generateReactJSComponent
    optionsJson = parserToJSON(parser, className)
    return generateReactJSComponent(className, optionsJson['options'])


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



def parserToMaterialUIJavascriptClass(parser, className = "Options"):
    classes = ["export class "+className+" {", "", "", "constructor() {"]
    
    classes.append("""       
           return (
       <Card  className="w-auto" color="white" shadow={true} children={
      <div className="p-10">
""")
          
    classes.append("""       
        <form className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">
""")
          


    classes.append("<Typography variant=\"h6\" color=\"blue-gray\" className=\"-mb-3\">")  
    classes.append("              "+ className)  
    classes.append("            </Typography>")  
    

    classes.append("")  
    classes.append("")  
    classes.append("// -------------- Help --------------")  
    
    classes.append("")  
        
    classes.append("")  
    classes.append("")  
    classes.append("}")  
    classes.append("")  
    classes.append("")  
    classes.append("""
                   </div>

       }/>
                   );
  }""")  
                
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



