from congruence import Congruence
from polynomial import Polynomial

def main():
    p = 13

    # Making Z_p
    mod_p = Congruence(p)

    # Defining an irreducible polynomial in F_p[Y]
    conway_polynomial_coefficients = [2, 1, 1, 8, 5, 7, 0, 0, 0, 0, 1]
    conway_polynomial_coefficients = [mod_p(k) for k in conway_polynomial_coefficients]

    conway_polynomial = Polynomial(conway_polynomial_coefficients, indeterminate='y')

    print('Conway polynomial', conway_polynomial)

    # Creating F_p^n
    GF13P10 = Congruence(conway_polynomial)

    # Testing product in F_p^n
    a = [1, 2]
    a = [mod_p(k) for k in a]
    a = Polynomial(a)
    a = GF13P10(a)
    
    b = [3, 0, 1]
    b = [mod_p(k) for k in b]
    b = Polynomial(b)
    b = GF13P10(b)

    c = a * b

    print('a = ', a.value.coefficients)
    print('b = ', b.value.coefficients)
    print('c = a*b = ', c.value.coefficients)







if __name__=="__main__":
    main()