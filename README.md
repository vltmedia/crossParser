# Description:
Parse a python argparse object into CSharp, Javascript, and Python classes.
This is useful for creating a GUI for a python script.

# Requirements:
- Python 3.6+

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
classString = crossParser.parserToCSharpClass(parser, className = "Options")
open(f"output\Options.cs", "w").write(classString)
open(f"output\Options.js", "w").write(parserToJavascriptClass(parser, className = "Options"))
open(f"output\Options.py", "w").write(parserToPythonClass(parser, className = "Options"))
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
