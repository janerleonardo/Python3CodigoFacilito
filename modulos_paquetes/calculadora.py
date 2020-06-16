"""
Modulo de calculadora para uso donde se necesite, esto subio un poco el nivel me estaba decepcionando
de python mucho
"""
def suma(val1,val2):
    """Documentacion de Metod suma ohoho"""
    return val1 + val2

def resta(val1,val2):
    return val1 - val2

def multiplicacion(val1,val2):
    return val1 * val2

def division(val1,val2):
    try:
        return val1 / val2
    except:
        print("Divicion por Cero")