import os, json, glob, sys

ImportForm = """
import {
    Card,
    Input,
    Checkbox,
    Button,
    Typography,
    Select, Option 
  } from "@material-tailwind/react";

  import {useState, useEffect} from "react"
"""

UseEffect = """
useEffect(() => {
    }, [])
"""

SubmitedClicked = """
    const submitClicked = (e) => {
    }
"""

def TopClassHeader  (className, props = [] ):
    propItems = []
    # for prop in props:
    #     propItems.append(f"{prop['name']} = {prop['default']}")
    return "export const "+className+" = ({"+" , ".join(propItems)+"}) => {"

def GenerateStates(props):
    stateItems = []
    for prop in props:
        val = prop['default']
        if val == "True" or val == True:
            val = "true"
        elif val == "False" or val == False:
            val = "false"
        stateItems.append(f"const [{prop['name'].replace(' ', '')}, set{prop['name'].replace(' ', '')}] = useState({val})")
    return "\n".join(stateItems)

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
        return f"<Checkbox label=\"{prop['name'].replace('_', ' ').capitalize()}\" value={{%LABELSET%}} onChange={{(e) => set%LABELSET%(e.target.value)}} />".replace("%LABELSET%", prop['name'].replace(' ', '')).replace("%DEFAULT%", str(val))
    return     """
                    <Typography variant="h6" color="blue-gray" className="-mb-3">
            %LABELNAME%
            </Typography>
            <Input
            size="lg"
            placeholder={%DEFAULT%}
            defaultValue={%DEFAULT%}
            value={%DEFAULT%}
            type="%TYPE%"
            className=" !border-t-blue-gray-200 focus:!border-t-gray-900"
            labelProps={{
                className: "before:content-none after:content-none",
            }}
            onChange={(e) => set%LABELSET%(e.target.value)}
            />
                    """.replace("%LABELNAME%", prop['name'].replace('_', ' ').capitalize()).replace("%LABELSET%", prop['name'].replace(' ', '')).replace("%DEFAULT%", str(val)).replace("%TYPE%", inputType)

def generateReactJSComponent(className, props = []):
    outArray = []
    outArray.append("")
    outArray.append(ImportForm)
    outArray.append("")

    outArray.append("")
    outArray.append(TopClassHeader(className, props))
    outArray.append("")
    outArray.append("")
    outArray.append(GenerateStates(props))
    outArray.append("")
    outArray.append("")
    outArray.append(UseEffect)
    outArray.append("")
    outArray.append(SubmitedClicked)
    outArray.append("")
    outArray.append("")
    outArray.append("    return (")
    outArray.append("""
                     <Card  className="w-auto" color="white" shadow={true} children={
      <div className="p-10">
        <form className="mt-8 mb-2 w-80 max-w-screen-lg sm:w-96">
          <div className="mb-1 flex flex-col gap-6">

          <Typography variant="h6" color="blue-gray" className="-mb-3">
                    """
                    )
    outArray.append(className)
    outArray.append("</Typography>")
    
    for prop in props:
        outArray.append("")
        outArray.append(GenerateInput(prop))
        outArray.append("")
        outArray.append("")
    outArray.append("""
                    </div>
        <Button className="mt-6" fullWidth onClick={submitClicked}>
            Submit
        </Button>
        </form>
</div>

    }/>
        

    );
}
                    """)
    
    return "\n".join(outArray)
    
    
        

    
    
    
    
    
    
    
    
    
