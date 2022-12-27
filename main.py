#TAYLOR POLYNOMIAL

from function import *


#Libraries.

import numpy as np
import sympy as sym

from sympy.parsing.sympy_parser import parse_expr #Function to read input and make it an equation.


#Data.

fx = parse_expr(input("Input equation: "))

x0 = int(input("Input x0: "))

n = int(input("Input degree n: "))


#Results.

polynomial = polytaylor(fx,x0,n)

print("Function: ")
sym.pprint(fx)

print("\nTAYLOR POLYNOMIAL:")
sym.pprint(polynomial)

