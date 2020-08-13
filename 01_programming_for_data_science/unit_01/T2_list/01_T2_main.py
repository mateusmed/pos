#video 1 apenas uma pequena intrudução a lista


def create_list():
    # 1 criando listas
    lista_vazia = []
    lista_vazia2 = list()

    type(lista_vazia)
    type(lista_vazia2)

    len(lista_vazia)

    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
    lista_reais = [1.5, -2.13, 5.14]
    lista_strings = ["exemplo1", "exemplo2", "exemplo3"]
    lista_booleanos = [True, True, False, True]
    lista_misturada = [1, 2, 3.14159, "teste"]
    lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
    listas_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(lista)
    print(lista_reais)
    print(lista_strings)
    print(lista_booleanos)
    print(lista_misturada)
    print(lista_misturada2)
    print(listas_aninhada)


def get_elements_of_list():
    # 2 acessando elementos da lista

    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
    lista_strings = ["exemplo1", "exemplo2", "exemplo3"]
    lista_misturada = [1, 2, 3.14159, "teste"]
    lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]

    print(lista[0])
    print(lista[2])
    print(lista_strings[3])
    print(lista_strings)
    print(lista_misturada[3])
    print(lista_misturada)
    print(lista_misturada2[4][1])
    print(lista_misturada2)
    print(lista[20])


def modify_elements_on_list():
    # 3 como modificar elementos de uma lista

    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]

    print(lista)
    lista[1] = 18
    print(lista)

    lista[3] = 15
    print(lista)

    lista[2] = lista[0] + lista[1]
    print(lista)


def methods_of_list():
    # 4 principais metodos do objeto lista

    # append
    append_example()
    # clear
    clear_example()
    # copy
    copy_example()
    # count
    copy_example()
    # extend
    extends_example()
    # index
    index_example()
    # insert
    insert_example()
    # pop
    pop_example()
    # remove
    remove_example()
    # reverse
    reverse_example()
    # sort
    sort_example()


def functions_to_apply_in_list():
    # 5 - funções aplicaveis a uma lista
    # len
    len_example()
    # max
    max_example()
    # min
    min_example()
    # sum
    sum_example()


def append_example():
    # append

    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]

    print(lista)
    lista.append(17)
    print(lista)


def clear_example():
    # clear
    lista_reais = [1.5, -2.13, 5.14]

    print(lista_reais)
    lista_reais.clear()
    print(lista_reais)


def copy_example():

    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]

    # copy
    copia = lista
    print(copia)

    copia[0] = 5
    print(copia)

    print(lista)
    lista[0] = 23

    copia = lista.copy()
    print(lista)
    print(copia)

    copia[0] = 5
    print(lista)
    print(copia)


def count_example():
    lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
    # count
    lista.count(5)


def extends_example():
    # extend
    numeros = [1, 2, 3]
    numeros.append([4, 5])  # adicionando uma nova lista
    print(numeros)

    numeros = [1, 2, 3]
    numeros.extend([4, 5])  # adicionando os items a lista original
    print(numeros)


def index_example():
    # index
    lista = [1, 3, 7, 2, 3, 8, 4]
    lista.index(7)

    posicao8 = lista.index(8)
    print(posicao8)

    posicao3 = lista.index(3)
    print(posicao3)

    lista.index(19)  # erro posicao não existe


def insert_example():
    lista = [1, 3, 7, 2, 3, 8, 4]

    lista.insert(1, "ABC")
    print(lista)

    lista.insert(100, "XYZ")
    print(lista)


def pop_example():
    lista = [1, 3, 7, 2, 3, 8, 4]

    valor = lista.pop(2)
    print(valor)

    print(lista)

    lista.pop(-1)
    print(lista)

    lista.pop(45) # erro posição não existe


def remove_example():
    lista_strings = ["exemplo1", "exemplo2", "exemplo3"]

    print(lista_strings)
    lista_strings.remove("exemplo1")

    print(lista_strings)

    lista_strings.remove("exemplo4") # erro item não existe


def reverse_example():
    lista = [6, 3, 1, 4, 2, 5]
    lista.sort(reverse=True)
    print(lista)


def sort_example():

    lista = [6, 3, 1, 4, 2, 5]
    lista.sort()

    print(lista)

    lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]

    lista_letras.sort()
    print(lista_letras)


def len_example():
    lista = [8, 3, 21, 14, 2, 45]

    tamanho = len(lista)
    print(tamanho)


def max_example():
    lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]

    max_of_list = max(lista_letras)
    print(max_of_list)


def min_example():
    lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]

    min_of_list = min(lista_letras)
    print(min_of_list)


def sum_example():
    lista = [8, 3, 21, 14, 2, 45]

    sum_of_list = sum(lista)
    print(sum_of_list)


def video2():
    methods_of_list()
    functions_to_apply_in_list()












