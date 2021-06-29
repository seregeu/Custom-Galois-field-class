import sympy as sp
from sympy.abc import x, y
from tabulate import tabulate
from galoislab import CustomGaloisField

def first_var():
    #gf = CustomGaloisField(x=x,p=2, n=1)
    #gf.print()
    #gf.simple_realization_operations()

    gf = CustomGaloisField(x=x, p=2, n=4, irr=sp.Poly(x**4+x+1, x))
    gf.print()
    gf.ext_realization_operations()

    #gf = CustomGaloisField(x=x, p=2, n=3+2, irr=sp.Poly(x**5 + x**2 + 1, x))
    #gf.print()
    #gf.ext_realization_operations()
    #gf.extend(y=y, n=2, ext_irr=sp.Poly(y ** 2 + (x + 1) * y + x ** 2 + x + 1, y, x))
    #gf.print_ext()
    #gf.ext_ext_realization_operations()

if __name__ == '__main__':
    first_var()
    #gf = CustomGaloisField(x=x,p=7, n=1)
    #gf.print()
    #gf.simple_realization_operations()
    #gf = CustomGaloisField(x=x, p=7, n=3, irr=sp.Poly(x ** 3 + 3 * x + 2, x))
    #gf.print()
    #gf.ext_realization_operations()

    #gf = CustomGaloisField(x=x, p=7, n=5, irr=sp.Poly(x ** 5 + x + 4, x))
    #gf.print()
    #gf.ext_realization_operations()

    #gf.extend(y=y, n=2, ext_irr=sp.Poly(y**2 + (6*x**2 + 6*x + 4)*y + 3*x**2, y, x))
    #gf.print_ext()
    #gf.ext_ext_realization_operations()


