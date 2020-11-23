# PythonLogicParser
Parses a String to a Logic Abstract Syntax Tree.

```python
from LParser import LogicParser

logic = "(x and (y or x)) or (o or (not (b and (a and a))))"
parser = LogicParser(logic)
tree = parser.tree

```
This tree has a standard node implementation with Node.node is "or" , "and", "not" or name_of_variable.
For testing you could use 

```python
from Util import print_level_order
printLevelOrder(tree)
```
