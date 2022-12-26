#Example!

from function import *

#Libraries

import numpy as np
import sympy as sym
#import matplotlib.pyplot as plt

#Data.

#x = sym.Symbol('x')

fx = (sym.cos(x)) / (2 * (1 + sym.cos(x))) #Function.

x0 = 0

n = 2 #Degree n.


#Results.

polynomial = polytaylor(fx,x0,n)

print("Function: ")
sym.pprint(fx)

print("\nTAYLOR POLYNOMIAL:")
sym.pprint(polynomial)


