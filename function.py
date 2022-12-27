"""
TAYLOR POLYNOMIAL
"""

#Libraries.

import numpy as np
import sympy as sym


"""
How to install -> README
"""

#Taylor Function.

x = sym.Symbol('x')

def polytaylor(fx, x0, n):

    k = 0
    polynomial = 0

    while (k <= n):
        dif = fx.diff(x,k)
        difx0 = dif.subs(x,x0)
        divisor = np.math.factorial(k)
        termk = (difx0 / divisor) * (x-x0) ** k
        polynomial = polynomial + termk
        k += 1

    return (polynomial)

"""
PLEASE LOOK UP ABOUT THE VARIABLES
"""

