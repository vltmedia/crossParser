import os, json, glob, sys

ImportForm = """
<!DOCTYPE html>
<html>
<body>

"""

def GenerateInput(prop):
    val = prop['default']
    typeBool = False
    if val == "True" or val == True:
        val = "true"
        typeBool = True
    elif val == "False" or val == False:
        val = "false"
        typeBool = True
    inputType = "text"
    if isinstance( prop['default'], int) or isinstance( prop['default'], float):
        inputType = "number"
    if typeBool:
        return      """
            %LABELNAME%
            <input id="%LABELSET%" name="%LABELSET%" type="checkbox"><br>
                    """.replace("%LABELNAME%", prop['name'].replace('_', ' ').capitalize()).replace("%LABELSET%", prop['name'].replace(' ', '')).replace("%DEFAULT%", str(val)).replace("%TYPE%", inputType)

    return     """
            %LABELNAME%
            <input placeholder=%DEFAULT% type="%TYPE%"><br>
                    """.replace("%LABELNAME%", prop['name'].replace('_', ' ').capitalize()).replace("%LABELSET%", prop['name'].replace(' ', '')).replace("%DEFAULT%", str(val)).replace("%TYPE%", inputType)

def generateHTMLForm(className, props = []):
    outArray = []
  
    outArray.append(f"<h2>{className}</h2>")
    outArray.append("")
    outArray.append("<form id=\"frm1\" >")
    
    for prop in props:
        outArray.append("")
        outArray.append(GenerateInput(prop))
        outArray.append("")
        outArray.append("")
    outArray.append("""
                      <input type="button" onclick="myFunction()" value="Submit">
</form>

<script>
function myFunction() {
  
}
</script>

                    """)
    
    return "\n".join(outArray)
    
    
def generateHTMLFormPage(className, props = []):
    outArray = []
    outArray.append("")
    outArray.append(ImportForm)
    outArray.append("")
    outArray.append(generateHTMLForm(className, props))
    outArray.append("""
</body>
</html>
                    """)
    
    return "\n".join(outArray)
    
    
        

    
    
    
    
    
    
    
    
    
