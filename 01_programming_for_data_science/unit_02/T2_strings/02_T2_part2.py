


def captilize_example():
    s = "a linguagem python é demais!"
    a = s.capitalize()
    print(a)

#mais agressivo que o lower
def case_fold_example():
    s = "AbCdEf"
    s1 = s.casefold()
    print(s1)

    # aplicando ao caracter especial: ß
    s = "Der Fluß"
    s2 = s.casefold()
    print(s2)

def lower_example():
    s = "AbCdEf"
    s2 = s.lower()
    print(s2)

    s = "Der Fluß"
    s2 = s.lower()
    print(s2)


def upper_example():
    s = "AbCdEf"
    s3 = s.upper()
    print(s3)


def center_example():
    s = "mateus"
    s1 = s.center(20)
    print(s1)

def count_example():
    s = "A linguagem Python é demais!"
    value = s.count("a")
    value2 = s.count("demais")
    print(value)
    print(value2)


def encode_example():
    s = "Mоето име е Päivi"
    s1 = s.encode()  # Codifica usando o UTF-8 por padrão

    print(s)
    print(s1)


def endswith_example():
    s = "A linguagem Python é demais!"
    value = s.endswith("demais!")  # True
    print(value)

    value2 = s.endswith("demais!", 12)
    print(value2)

    str_test = s[2:18]
    print(str_test)

    value3 = s.endswith("Python", 2, 18)
    print(value3)


def expand_tabs_example():
    s = "col1\tcol2\tcol3"
    print(s)

    s1 = s.expandtabs() # Substitui as tabulações por espaços (default = 8)
    print(s1)

    print("--------")
    print("Tabsize =  5", s.expandtabs(20)) # para adicionar mais espaço na tabulação passar o numero de 'espaços'


def example_find():
    s = "A linguagem Python é demais! Python é sensacional."
    value = s.find("Python")
    print("primeiro python encontrado e é iniciado no index: ", value)


def example_r_find():
    s = "A linguagem Python é demais! Python é sensacional."
    value = s.rfind("Python")
    print("segundo python encontrado e é iniciado no index: ", value)


def example_index():
    s = "A linguagem Python é demais! Python é sensacional."
    value = s.index("Python")
    print(value)


def format_example():
    nome = "Joaquim"
    idade = 60
    print("Meu nome é {} e tenho {} anos.".format(nome, idade))

    print("Meu nome é {name} e tenho {age} anos.".format(age=18,
                                                         name="Pedro"))


def indentification_example():
    a = "12345"
    b = "1234²"
    c = "123²½"
    print("a.isdecimal() = ", a.isdecimal())
    print("b.isdecimal() = ", b.isdecimal())
    print("c.isdecimal() = ", c.isdecimal())
    print("=" * 25)
    print("a.isdigit() = ", a.isdigit())
    print("b.isdigit() = ", b.isdigit())
    print("c.isdigit() = ", c.isdigit())
    print("=" * 25)
    print("a.isnumeric() = ", a.isnumeric())
    print("b.isnumeric() = ", b.isnumeric())
    print("c.isnumeric() = ", c.isnumeric())



def isprintable_example():
    s = "col1\tcol2"
    s.isprintable()

    s1 = s.expandtabs()
    s1.isprintable()

    s2 = "linha1\nlinha2"
    s2.isprintable()


def isspace_example():
    s1 = "A B"
    value = s1[0].isspace()
    print(value)


def istitle_example():
    titulo = "A Linguagem Python"
    value = titulo.istitle()
    print(value)

    titulo = "A linguagem Python"
    value = titulo.istitle()
    print(value)


def pares():
    pares = list(range(2, 101, 2))
    print(pares)


def bissexto():
    # value = [ano for ano in range(1900, 2021, 4) if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)]

    # value = list(filter(lambda ano: (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0), range(1900, 2021, 4)))
    # print(value)

    value = list(range(1900, 2021, 4))
    print(value)

def test():
    # numeros = [n for n in range(1, 16)]
    # value = filter(lambda x: x % 3 == 0, numeros)
    # print(value)

    bissextos = [ano for ano in range(1900, 2021, 4) if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)]
    print(bissextos)

def main():
    captilize_example()

    # case_fold_example == lower_example
    # case_fold_example()
    # lower_example()
    # upper_example()
    # center_example()
    # count_example()
    # encode_example()
    # endswith_example()
    # expand_tabs_example()
    # example_find()
    # example_r_find()
    # example_index()
    # format_example()
    # indentification_example()
    # isspace_example()
    # istitle_example()
    #pares()
    # bissexto()
    test()

main()