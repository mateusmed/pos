import numpy as np


def create_array_one_dimension():
    a1D= np.array([1, 2, 3])
    print(a1D)


def type_array():
    a1D = np.array([1, 2, 3])
    print(type(a1D))


def float_type_narray():
    my_array = np.array([1, 2, 3], dtype=float)
    print(type(my_array[0]))


def string_type_narray():
    my_array = np.array([1, 2, 3], dtype=str)
    print(type(my_array[0]))


def n_types_narray():

    # todos serão string
    # str > float > int > bool
    my_array = np.array([1, 3.14, "numPy", True])
    print(type(my_array[0]))


def create_array_two_dimension():
    a2d = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
    print(a2d)


def create_array_three_dimension():
    a2d = np.array([ [ [1, 2, 3], [4, 5, 6] ], [ [7, 8, 9], [10, 11, 12] ], [ [13, 14, 15], [16, 17, 18] ]])
    print(a2d)


def array_zeros_one_dimension():
    # 1 dimensão
    azeros = np.zeros(5)
    print(azeros)


def array_zeros_two_dimension():
    azeros = np.zeros((3, 4)) # 3 linhas 4 colunas
    print(azeros)


def array_zeros_three_dimension():
    azeros = np.zeros((3, 4, 2)) # 3 paginas 4 linhas e 2 colunas
    print(azeros)


def create_array_with_values():
    # cria um narray preenchido com os elementos de 0 a n-1
    a1d = np.arange(10)
    print(a1d)

    # criando de 5 até 14
    a1d = np.arange(5, 15)
    print(a1d)

    # criando de 5 até 99 variando de 10 em 10
    a1d = np.arange(5, 100, 10)
    print(a1d)

    a3d = np.full((3, 5, 8), -1) # ndarray de 3 paginas, 5 linhas e 8 colunas com o valor -1
    print(a3d)


def main_matriz():
    # criando matriz principal com 5 linhas e 5 colunas
    # lembrando q uma matriz principal, sempre possui o mesmo valor de linhas e colunas
    ident = np.eye(5)
    print(ident)


def create_random_array():
    # criando 10 elementos aleatorios entre 0 e 99
    a1d = np.random.randint(0, 100, 10)
    print(a1d)

    # criando numeros aleatorios em uma matriz 4 por 5
    a2d = np.random.randint(1, 500, (4, 5))
    print(a2d)

    # criando numeros aleatorios de 1 a 60 em 10 cubos de 1 linha e 6 colunas
    a3d = np.random.randint(1, 61, (10, 1, 6))
    print(a3d)

    # gerando 10 elementos de numeros aleatorios em 0 e 1
    b1d = np.random.random(10)
    print(b1d)


def main():
    create_array_one_dimension()
    type_array()
    float_type_narray()
    string_type_narray()
    n_types_narray()
    create_array_two_dimension()
    create_array_three_dimension()
    array_zeros_one_dimension()
    array_zeros_two_dimension()
    array_zeros_three_dimension()
    create_array_with_values()
    main_matriz()
    create_random_array()


main()
