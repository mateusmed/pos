
# video 1 nada de importante


def create_sets():
    # exemplos de diferença entre dict e sets

    conj_vazio1 = set()
    type(conj_vazio1)

    dict = {}
    conj1 = {1, 2, 3, 4, 5}

    conjLetters = {"A", "B", "C", "D", "E"}

    # por default é um dict (semelhante a um json)
    # se nao tiver chave e valor é um conjunto

    print(type(dict))
    print(type(conj1))
    print(type(conjLetters))

    dict = {"key": "Value"}
    print(dict)
    print(type(dict))

    # não é possível ter um conjunto complexo
    conj3 = {1, "ABC", [1, 2, 3]}


def access_elements_of_sets():
    # conjuntos não são indexados, não é possível acessar uma posição

    conj1 = {1, 2, 3, 4, 5}

    for elem in conj1:
        print(elem)

    print(conj1[0]) # error


def modify_elements_of_set():
    # Nâo existe uma maneira de modificar elementos em um conjunto.
    # O que pode ser feito é a exclusão de um elemento, seguida da inserção de outro elemento

    conj1 = {1, 2, 3, 4, 5}
    conj1.remove(3)

    print(conj1)

    conj1.add(3)

    print(conj1)


def add_element_example():
    conj1 = {1, 2, 3, 4, 5}
    conj1.add(6)


def clear_element_example():
    conj = {1, 2, 3, 4, 5}
    print(conj)
    conj.clear()
    print(conj)


def copy_element_example():
    conj1 = {1, 2, 3, 4, 5}
    conj3 = conj1.copy()
    print(conj3)


def difference_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    s3 = s1.difference(s2)
    print("s1 - s2 = ", s3)

    s4 = s2.difference(s1)
    print("s2 - s1 = ", s4)


def intersection_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    s3 = s1.intersection(s2)
    print("s1 - s2 = ", s3)


def isdisjoint_example():
    # Verificando se s1 e s2 são disjuntos
    # Em matemática, dois conjuntos são ditos disjuntos se não tiverem nenhum elemento em comum

    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    print(s1.isdisjoint(s2))


def issubset_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    # verificando se s1 é um subconjunto de s2
    print(s1.issubset(s2))

    s3 = {1, 2, 3, 4, 5}
    s4 = {1, 2, 3, 4, 5, 6, 7, 8}

    print(s3.issubset(s4))


def issuperset_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    # verificando se s1 possui tudo que tem em s2
    print(s1.issuperset(s2))

    s3 = {1, 2, 3, 4, 5}
    s4 = {1, 2, 3, 4, 6, 5, 7, 8}

    # verificando se s4 possui tudo que tem em s3
    print(s4.issuperset(s3))


def remove_element_example():
    conj1 = {1, 2, 3, 4, 5}
    conj1.remove(3)
    print(conj1)


def discart_element_example():
    conj1 = {1, 2, 3, 4, 5}
    conj1.discard(3)
    print(conj1)


def remove_discart_example():
    remove_element_example()
    discart_element_example()


def symmetric_difference_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    # cria um novo conjunto removendo os itens em comum
    s5 = s1.symmetric_difference(s2)
    print(s5)


def union_example():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7}

    s6 = s1.union(s2)
    print(s6)


def main_methods_of_sets():
    # add
    add_element_example()
    # clear
    clear_element_example()
    # copy
    copy_element_example()
    # difference
    difference_example()
    # intersection
    intersection_example()
    # isdisjoint
    isdisjoint_example()
    # issubset
    issubset_example()
    # issuperset
    issuperset_example()
    # remove || discart
    remove_discart_example()
    # symmetric_difference
    symmetric_difference_example()
    # union
    union_example()


def class_sets():
    # criando conjuntos
    create_sets()
    # acessando elementos de um conjunto
    access_elements_of_sets()
    # modificando elementos de um conjunto
    modify_elements_of_set()
    # principais metodos de um objeto conjunto
    main_methods_of_sets()


