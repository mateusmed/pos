

# video 1 definição simples de dicionario
# chave_valor -- dict != json


def create_dictionary():
    dict_vazio1 = {}
    dict_vazio2 = dict()

    print(type(dict_vazio1))

    isinstance(dict_vazio2, dict)


def set_get_value_of_dictionary():
    dic_estados = {"MG": "Minas Gerais",
                   "PR": "Paraná",
                   "BA": "Bahia",
                   "RN": "Rio Grande do Norte",
                   "AM": "Amzonas"}

    print(dic_estados["PR"])

    print(dic_estados["XYZ"]) # return error

    dic_produtos = {1215: "Lápis",
                    3221: "Caneta",
                    2329: "Borracha",
                    1092: "Caderno",
                    7633: "Cola"}

    print(dic_produtos[2329])

    dic_notas_alunos = {"João": [30, 12, 21],
                        "Maria": [20, 30, 29],
                        "José": [20, 23, 19]}

    nome_aluno = "Maria"
    print("As notas de " + nome_aluno + " foram: " + str(dic_notas_alunos[nome_aluno]) + ".")


    print(nome_aluno+" tirou "+str(dic_notas_alunos[nome_aluno][0])+" pontos na 1a prova.")

    dic_notas_alunos2 = {
                            "João": {"nota1": 30,
                                     "nota2": 12,
                                     "nota3": 21},

                            "Maria": {"nota1": 20,
                                      "nota2": 30,
                                      "nota3": 29},

                            "José": {"nota1": 20,
                                     "nota2": 23,
                                     "nota3": 19},
                        }

    print(dic_notas_alunos2)
    print(dic_notas_alunos2["João"]["nota1"])


def modify_value_of_dictionary():
    dic_estados = {"MG": "Minas Gerais",
                   "PR": "Paraná",
                   "BA": "Bahia",
                   "RN": "Rio Grande do Norte",
                   "AM": "Amzonas"}

    dic_estados["AM"] = "Amazonas"
    print(dic_estados)

    dic_notas_alunos = {"João": [30, 12, 21],
                        "Maria": [20, 30, 29],
                        "José": [20, 23, 19]}

    dic_notas_alunos["João"][1] = 22
    print(dic_notas_alunos)

    dic_notas_alunos["Maria"] = [25, 20, 22]
    print(dic_notas_alunos)

    dic_notas_alunos2 = {
        "João": {"nota1": 30,
                 "nota2": 12,
                 "nota3": 21},

        "Maria": {"nota1": 20,
                  "nota2": 30,
                  "nota3": 29},

        "José": {"nota1": 20,
                 "nota2": 23,
                 "nota3": 19},
    }

    dic_notas_alunos2["José"]["nota3"] = 25
    print(dic_notas_alunos2)


def clear_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    print(dic_exemplo)

    dic_exemplo.clear()
    print(dic_exemplo)


def copy_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    print(dic_exemplo)

    dic_exemplo2 = dic_exemplo.copy()
    print(dic_exemplo2)


def fromkeys_dict_example():
    dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10])
    print(dic_num_pares) # value none

    dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
    print(dic_num_pares) # adiciona par para todos os itens dessa lista


def get_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    dic_exemplo.get(2)


def itens_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    dic_exemplo.items()


def keys_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    dic_exemplo.keys()


def pop_dict_example():
    dic_exemplo = {1: "um", 2: "dois", 3: "três", 4: "quatro"}
    dic_exemplo.pop(1)
    print(dic_exemplo)

    valor = dic_exemplo.pop(4)
    print(valor)

def pop_item_dict_example():
    dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
    removido = dic_num_pares.popitem()
    print(removido)
    print(dic_num_pares)


def set_defatul_dict_example():
    dic_estados = {"MG": "Minas Gerais",
                   "PR": "Paraná",
                   "BA": "Bahia",
                   "RN": "Rio Grande do Norte",
                   "AM": "Amzonas"}

    dic_estados.setdefault("MG")
    print(dic_estados)

    dic_estados.setdefault("ES")
    print(dic_estados)

    dic_estados.setdefault("SC", "Santa Catarina")
    print(dic_estados)


def update_dict_example():
    dic_estados_centro_oeste = {"MS": "Mato Grosso do Sul", "TO": "Tocantins", "GO": "Goiás"}
    print(dic_estados_centro_oeste)

    dic_estados = {"MG": "Minas Gerais",
                   "PR": "Paraná",
                   "BA": "Bahia",
                   "RN": "Rio Grande do Norte",
                   "AM": "Amzonas"}

    dic_estados.update(dic_estados_centro_oeste)
    print(dic_estados)


def values_dict_example():
    dic_estados = {"MG": "Minas Gerais",
                   "PR": "Paraná",
                   "BA": "Bahia",
                   "RN": "Rio Grande do Norte",
                   "AM": "Amzonas"}

    print(dic_estados.values())


def main_methods_of_dictionary():
    # clear
    clear_dict_example()
    # copy
    copy_dict_example()
    # fromkeys
    fromkeys_dict_example()
    # get
    get_dict_example()
    # items
    itens_dict_example()
    # keys
    keys_dict_example()
    # pop
    pop_item_dict_example()
    # popitem
    pop_item_dict_example()
    # setdefault
    set_defatul_dict_example()
    # update
    update_dict_example()
    # values
    values_dict_example()


def video2():
    # como criar dicionarios
    create_dictionary()
    # 2. Acessando um valor em um dicionário através de uma chave
    set_get_value_of_dictionary()
    # 3. Modificando valores em um dicionário
    modify_value_of_dictionary()
    # 4. Principais métodos de um objeto dicionário
    main_methods_of_dictionary()

