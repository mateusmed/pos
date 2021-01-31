def simple_example():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    if x < y:
        print("{} é menor que {}.".format(x, y))
    elif x == y:
        print("{} é igual a {}.".format(x, y))
    else:
        print("{} é maior que {}.".format(x, y))