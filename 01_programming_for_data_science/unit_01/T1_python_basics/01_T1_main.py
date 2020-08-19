# video 1 - apenas explicando os tipos de dados
# - nenhuma informaçõa relevante


# video 2 - identificadores (variaveis)
# - exemplos bem simples dos padrão de variavel
# no PEP8 - Guido van Rossum sugere que nomes de variaveis
# deve ter apenas letra minúsculas e utilizar e undescore como separador


# video 3
# exemplos de dados

def video3():
    qtde = 5
    type(qtde)

    preco_produto = 125.50
    type(preco_produto)

    nome = "Maria"
    type(nome)

    tem_casa = True
    type(tem_casa)

    total_compra = qtde * preco_produto
    print(total_compra)


# video 4
# conversão de tipos, casting
def video4():
    # exemplos:
    int_string = str(5)
    string_float = float("3.14159")
    string_int = int("2019")
    int_bool = bool(17)

    #conversões para string:
    bool_string = str(True)
    bool_string2 = str(False)
    int_string = str(5)
    fload_string = str(3.14159)

    #conversões para int
    string_int = int("2019")
    bool_int = int(True)
    bool_int2 = int(False)
    fload_int = int(3.14159)
    string_int2 = int("101", 2) # base binaria
    string_int3 = int("F0A23B", 16) # base 16

    #conversões para Float
    string_float = float("3.1415159")
    string_float2 = float("3")
    bool_float = float(True)
    bool_float2 = float(False)
    int_fload = float(15)

    # conversões para bool
    # qualquer valor != 0 é considerado com true
    string_bool = bool("Python")
    string_bool2 = bool("True")
    string_bool3 = bool("False")  # pegadinha, retorna True
    int_bool = bool(17)
    int_bool2 = bool(0)
    float_bool = bool(3.14)
    float_bool = bool(0.0)


# video 5 - comentarios
def video5():
    # um simples comentario
    """
    isso é um comentario
    com mais de uma linha
    """