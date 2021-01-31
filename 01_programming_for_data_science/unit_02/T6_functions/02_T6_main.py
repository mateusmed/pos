
def potencia(num, pot):
    return num ** pot


def test_potencia():
    c = potencia(5, 2)
    print(c)


# lambda num, pot: num ** pot
# Definida dessa forma, a expressão lambda fica sem referência para uso posterior.
def test_function_lambda():
    lambda_pot = lambda num, pot: num ** pot  # Podemos então atribuir a expressão lambda
    d = lambda_pot(3, 4)
    print(d)