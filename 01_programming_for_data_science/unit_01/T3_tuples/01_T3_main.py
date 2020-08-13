

# video 1
# tupla é semelhante a lista, mas com o principio de imutabilidade


# video 2

def video2():
    # 1 - como criar uma tupla
    create_tuple_example()
    # 2 - como acessar elementos da uma tupla
    access_elements_of_tuple()
    # 3 - imutabilidade da tupla
    imutability_example()
    # 4 - principais métodos de um objeto tupla
    main_methods_of_tupla()
    # 5 - funções aplicáveis a uma tupla
    functions_apply_tupla()
    # 6 - convertendo uma tupla em lista
    convert_tupla_in_list()


def access_elements_of_tuple():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
    tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])

    print(tupla1[0])
    print(tupla1)

    print(tupla2[5])
    print(tupla2)

    print(tupla3[8])
    print(tupla3)

    print(tupla3[20])  # error


def imutability_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
    tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])

    tupla2[1] = "imutável" # tupla não permite atribuição

    tupla2[8][1] = 5

    # Podemos adicionar elementos à lista armazenada no índice 8 da tupla
    tupla3[8].extend([4, 5, 6])

    tupla3[8] = [-1, -2, -3] # erro


def main_methods_of_tupla():
    count_tuple_example()
    index_of_tuple_example()


def count_tuple_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)

    print(tupla1)

    print(tupla1.count(3))


def index_of_tuple_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)

    print(tupla1)

    print(tupla1.index(21))


def functions_apply_tupla():
    len_example()
    max_example()
    min_example()
    sum_example()


def len_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    print(len(tupla1))


def max_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    print(max(tupla1))


def min_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    print(min(tupla1))


def sum_example():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    print(sum(tupla1))


def convert_tupla_in_list():
    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    lista = list(tupla1)

    # A imutabilidade da tupla não permite a alteração de um valor
    tupla1[6] = -1

    lista[6] = -1
    print(lista)


def create_tuple_example():
    tupla_vazia = ()
    tupla_vazia2 = tuple()

    type(tupla_vazia)

    print(isinstance(tupla_vazia, tuple))

    len(tupla_vazia)

    tupla1 = (3, 19, 4, 21, 3, 5, 13)
    tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla", (1, 2, 3))
    tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])

    print(tupla1)
    print(tupla2)
    print(tupla3)


