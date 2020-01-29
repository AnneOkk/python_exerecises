import make_module

## module_name.function_name
make_module.make_module('modules store functions', 'create a module', 'import the module in new file')

## import only the function
from make_module import make_module
make_module('modules store functions', 'create a module', 'import the module in new file')

## using an alias for the imported function
from make_module import make_module as mm
mm('modules store functions', 'create a module', 'import the module in new file')

## using an alias for the module
import make_module as make
make.make_module('modules store functions', 'create a module', 'import the module in new file')

## importing all functions in a module
from make_module import *
make_module('modules store functions', 'create a module', 'import the module in new file')