#Example!

"""
Made by Jose Minuche.
"""

from function import *


#Libraries

import numpy as np
import sympy as sym


#Data.

fx = (sym.cos(x)) / (2 * (1 + sym.cos(x))) #Function.

x0 = 0 #x0

n = 2 #Degree n.


#Results.

polynomial = polytaylor(fx,x0,n)

print("Function: ")
sym.pprint(fx)

print("\nTAYLOR POLYNOMIAL:")
sym.pprint(polynomial)


