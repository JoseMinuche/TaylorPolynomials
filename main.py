#TAYLOR POLYNOMIAL

#Libraries.

import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

from sympy.parsing.sympy_parser import parse_expr #Function to read input and make it an ecuation.

from function import *


#Data.

fx = parse_expr(input("Input ecuation: "))

x0 = int(input("Input x0: "))

n = int(input("Input degree n: "))


#Results.

polynomial = polytaylor(fx,x0,n)

print("Function: ")
sym.pprint(fx)

print("\nTAYLOR POLYNOMIAL:")
sym.pprint(polynomial)

