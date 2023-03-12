
"""
Sofia Valero Martinez
"""


def esPrimo(numero):

    """
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    for prova in range(2, int(numero**0.5)+1):
        if numero % prova == 0:
            return False
    return True




def primos(numero):

    '''
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    '''

    return tuple([prova for prova in range(2, numero) if esPrimo(prova)])




def descompon(numero):
    
    """
    Devuelve una tupla con la descomposicion en factores
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """

    factores = [] #lista vacia

    for factor in primos(numero):
        while numero%factor == 0:
            factores.append(factor) #añadir factor a factores
            numero //= factor 
    return tuple(factores)


def dicFact(numero1, numero2):

    factores1 = descompon(numero1) #descomposicio 1
    factores2 = descompon(numero2) #descomposicio 2
    factores = set(factores1 + factores2) #set suma de dos tuplas 
    dicFact1 = {factor: 0 for factor in factores} #inicialitzar a 0
    dicFact2 = {factor: 0 for factor in factores} 
    for factor in factores1: dicFact1[factor] += 1 
    for factor in factores2: dicFact2[factor] += 1
    return dicFact1, dicFact2

    
def mcm(numero1, numero2):

    """
    >>> mcm(90, 14)
    630
    """

    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor], dicFact2[factor])
    return mcm


def mcd(numero1, numero2):

    """
    >>> mcd(924, 780)
    12
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor], dicFact2[factor])
    return mcd


import doctest
doctest.testmod()
