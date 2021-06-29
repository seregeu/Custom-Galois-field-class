import sympy as sp
from sympy.abc import x, y
from tabulate import tabulate


class CustomGaloisField:
    def __init__(self, x: sp.Symbol, p: int, n: int, irr: sp.Poly=None):
        # Extension parameters
        self.ext_elements = None
        self.ext_irr = None
        self.y = None
        self.p = p
        self.n = n
        self.irr = irr
        self.x = x

        self.dim = p**n
        # Initial elements
        self.elements=[]
        #If field is simple
        if n==1:
            self.primitive = sp.primitive_root(self.p)
            for i in range(0, self.dim):
                el = i
                self.elements.append(el)
            self.irr = p
            return
        self.elements = [sp.Poly(0, self.x, modulus=self.p)] + \
                        [sp.Poly(self.x ** i, self.x, modulus=self.p) for i in range(n)]
        self.primitive = x
        print(self.elements)
        for i in range(n, self.dim):
            el = sp.rem(
                sp.Poly(self.x ** i, x), self.irr,
                modulus=p, symmetric=False
                        )
            if el not in self.elements:
                self.elements.append(el)
                #print(el.args[0])
            #    if len(self.elements)==10:
            #        print("\nAddition")
            #        self._create_table(self.elements, lambda p1, p2: p1 + p2)
            #        print("\nMultiplication")
             #       self._create_table(self.elements,
             #                          lambda p1, p2: sp.rem(p1 * p2, self.irr, modulus=self.p, symmetric=False))

            else:
                if el == 1 and len(self.elements) == self.dim:
                    print('Last element is 1. Irreducible polynomial is primitive.')
                else:
                    raise ValueError(
                        'Repeated field element detected; please make sure your irreducible polynomial is primitive.')

    def extend(self, y: sp.Symbol, n: int, ext_irr: sp.Poly):
        self.y = y
        self.ext_irr = ext_irr
        self.ext_elements = [sp.Poly(0, self.ext_irr.gens[::-1], modulus=self.p)] + \
                            [sp.Poly(self.y ** i, self.ext_irr.gens[::-1], modulus=self.p) for i in range(n)]
        print ("size =",self.dim ** n )

        for i in range(n, self.dim ** n):

            el = sp.rem(
                sp.Poly(self.y ** i, self.y), self.ext_irr,
                modulus=self.p, symmetric=False
            )

            el = sp.rem(
                sp.Poly(el, el.gens[::-1]), self.irr,
                modulus=self.p, symmetric=False
            )

            if el not in self.ext_elements:
                self.ext_elements.append(el)
                #print(el.args[0])

            else:
                if el == 1 and len(self.elements) == self.dim:
                    print('Last element is 1. Irreducible polynomial is primitive.')
                else:
                    raise ValueError(
                        'Repeated field element detected; please make sure your irreducible polynomial is primitive.')

    def print(self):
        print(f'{len(self.elements)} elements:')
        print(f'primitive:{self.primitive}')
        print(f'characteristic:{self.p}')
        if (self.n!=1):
            print(f'expansion digit:{self.n}')
            for el in self.elements:
                print(el.args[0])
        else:
            for el in self.elements:
                print(el)

    def print_ext(self):
        print(f'{len(self.ext_elements)} elements:')
        print(f'expansion digit:{self.n}')
        print(f'primitive:{self.primitive}')
        print(f'characteristic:{self.p}')
        for el in self.ext_elements:
            print(el.args[0])

    def simple_create_table(self, elements, func):
        table = [elements]

        for i in elements:
            row = [i]

            for j in elements:
                row.append(func(i, j))
            table.append(row)

        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def _create_table(self, elements, func):
        table = [[el.args[0] for el in elements]]

        for i in elements:
            row = [i.args[0]]

            for j in elements:
                row.append(func(i, j).args[0])
            table.append(row)

        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))

    def _mult_ext(self, p1, p2):
        res = p1 * p2

        res = sp.rem(
            sp.Poly(res, res.gens[::-1]), sp.Poly(self.ext_irr),
            modulus=self.p, symmetric=False
        )

        res = sp.rem(
            sp.Poly(res, res.gens[::-1]), sp.Poly(self.irr),
            modulus=self.p, symmetric=False
        )

        return res

    def simple_realization_operations(self):
        irr = x+1
        p = self.p
        elements=[]
        for i in range(0, p):
            elements.append(self.elements[i])
        print("\nMultiplication")
        self.simple_create_table(elements.copy(), lambda p1, p2: sp.rem(p1 * p2, irr, modulus=p, symmetric=False))
        print("\nAddition")
        self.simple_create_table(elements.copy(), lambda p1, p2: sp.rem(p1 + p2, x ** p, modulus=p, symmetric=False))

    def ext_realization_operations(self):
        print("\nAddition")
        self._create_table(self.elements, lambda p1, p2: p1 + p2)
        print("\nMultiplication")
        self._create_table(self.elements, lambda p1, p2:sp.rem(p1 * p2, self.irr, modulus=self.p, symmetric=False))

    def ext_ext_realization_operations(self):
        print("\nAddition")
        self._create_table(self.ext_elements, lambda p1, p2: p1 + p2)
        print("\nMultiplication")
        self._create_table(self.ext_elements, self._mult_ext)

