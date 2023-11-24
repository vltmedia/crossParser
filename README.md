# Description:
Parse a python argparse object into CSharp, Javascript,React component, HTML Form, and Python classes.
This is useful for creating a GUI for a python script.

# Generates:
- CSharp Class
- CSharp Unity Monobehavior Form
- CSharp Unity UAI Form
- Javascript Class
- Javascript React Tailwind Material UI Component
- Python Class
- HTML Form
- HTML Form Page

# Requirements:
### Install/Dev
- Python 3.6+

### React Tailwind Material UI Component
To use the React component, you must install the following:
[Installation of the module](https://www.material-tailwind.com/docs/react/guide/cra)
```bash
npm i @material-tailwind/react
```

# Usage:
```python

import argparse 
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--gpu_ids', type=str, default='0', help='gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU')
parser.add_argument('--checkpoints_dir', type=str, default='./checkpoints', help='models are saved here')

        # input/output sizes
parser.add_argument('--batchSize', type=int, default=1, help='input batch size')
parser.add_argument('--loadSize', type=int, default=256, help='scale images to this size')
parser.add_argument('--fineSize', type=int, default=256, help='then crop to this size')
parser.add_argument('--input_nc', type=int, default=3, help='# of input image channels')
parser.add_argument('--output_nc', type=int, default=3, help='# of output image channels')

import crossParser
open(f"output\{className}.cs", "w").write(crossParser.parserToCSharpClass(parser, className = className))
open(f"output\{className}.js", "w").write(crossParser.parserToJavascriptClass(parser, className = className))
open(f"output\{className}.py", "w").write(crossParser.parserToPythonClass(parser, className = className))
open(f"output\{className}_uai.cs", "w").write(crossParser.generateUAIForm(parser, className = className))
open(f"output\{className}_unity.cs", "w").write(crossParser.generateUnityForm(parser, className = className))
open(f"output\{className}_react.js", "w").write(crossParser.parserToReactTailwindMaterialComponent(parser, className = className))
open(f"output\{className}_page_.html", "w").write(crossParser.parserToHTMLFormPage(parser, className = className))
open(f"output\{className}_form_.html", "w").write(crossParser.parserToHTMLForm(parser, className = className))
```

# Example Output:
### CSharp
```csharp
public class Options {


public string gpu_ids = "0";
public string checkpoints_dir = "./checkpoints";
public int batchSize = 1;
public int loadSize = 256;
public int fineSize = 256;
public int input_nc = 3;
public int output_nc = 3;

}
```

### Javascript
```javascript
export class Options {


constructor() {
this.gpu_ids = "0";
this.checkpoints_dir = "./checkpoints";
this.batchSize = 1;
this.loadSize = 256;
this.fineSize = 256;
this.input_nc = 3;
this.output_nc = 3;

}

}
```


### Python
```python
class Options:


    def __init__(self):
        self.gpu_ids = "0"
        self.checkpoints_dir = "./checkpoints"
        self.batchSize = 1
        self.loadSize = 256
        self.fineSize = 256
        self.input_nc = 3
        self.output_nc = 3
```
