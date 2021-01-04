
def strings_example():
    # com aspas simples
    hello_world = 'Hello world!!!'

    # com aspas duplas
    hello_world = "Hello world!!!"

    im_teacher = "I'm a teacher."
    variable = 'Ele é "bonito"... kkk'

    nome = "Joaquim"
    print(name)

    type(name)
    len(name)

    s = "Python"
    print(s[0])  # P
    print(s[1])  # y
    print(s[2])  # t
    print(s[3])  # h
    print(s[4])  # o
    print(s[5])  # n


def last_position_option_1():
    s = "Python"
    result = s[5]
    print("last position ", result)


def last_position_option_2():
    s = "Python"
    print("last position ", s[len(s)-1])


def last_position_option_3():
    s = "Python"
    result = s[-1]
    print("last position ", result)


def range_string_1():
    s = "Jupyter Notebook"
    result = s[0:7]
    print("result 1", result)


def range_string_2():
    s = "Jupyter Notebook"
    result = s[-16:-9]
    print("result 2", result)

def range_string_3():
    s = "Jupyter Notebook"
    result = s[:7]
    print("result 3", result)


def range_string_4():
    s = "Jupyter Notebook"
    result = s[:-9]
    print("result 4", result)


def range_string_5():
    s = "Jupyter Notebook"
    result = s[8:16]
    print("result 5", result)

def range_string_6():
    s = "Jupyter Notebook"
    result = s[-8:]
    print("result 6", result)

def range_string_7():
    s = "Jupyter Notebook"
    result = s[8:]
    print("result 7", result)

def range_string_8():
    s = "Jupyter Notebook"
    # o ultimo :2 significa incremento 2
    result = s[0:7:2]
    print("result 8", result)


def range_string_9():
    s = "Jupyter Notebook"
    # todas as posições com incremento de 3
    result = s[::3]
    print("result 9", result)


def range_string_10():
    s = "Jupyter Notebook"
    # mesmo processo mas com a string invertida
    # da posição -1 até o início, com incremento -1
    result = s[-1::-1]
    print("result 10", result)

def range_string_11():
    s = "Jupyter Notebook"
    # da posição -1 até o início, com incremento -1
    result = s[-1:-17:-1]
    print("result 11", result)


def range_string_12():
    s = "Jupyter Notebook"
    # da posição 16 até p início, com incremento -1
    result = s[16::-1]
    print("result 12", result)


def range_string_13():
    s = "Jupyter Notebook"
    # do final até o início, com incremento -1
    result = s[::-1]
    print("result 13", result)



def parts_of_string_1():
    # Acessando partes do string, a partir do início
    print("============ parts_of_string_1")
    p = "Python"
    print(p[:0])  # ''
    print(p[:1])  # 'P'
    print(p[:2])  # 'Py'
    print(p[:3])  # 'Pyt'
    print(p[:4])  # 'Pyth'
    print(p[:5])  # 'Pytho'
    print(p[:6])  # 'Python'
    print(p[:])  # 'Python'


def parts_of_string_2():
    print("============ parts_of_string_2")
    p = "Python"
    print(p[0:1])  # 'P'
    print(p[0:2])  # 'Py'
    print(p[0:3])  # 'Pyt'
    print(p[0:4])  # 'Pyth'
    print(p[0:5])  # 'Pytho'
    print(p[0:6])  # 'Python'
    print(p[0:])  # 'Python'



def parts_of_string_3():
    # Acessando partes do string, de uma posição qualquer até o final
    print("============ parts_of_string_3")
    p = "Python"
    print(p[:])  # 'Python'
    print(p[0:]) # 'Python'
    print(p[1:]) # 'ython'
    print(p[2:]) # 'thon'
    print(p[3:]) # 'hon'
    print(p[4:]) # 'on'
    print(p[5:]) # 'n'
    print(p[6:]) # ''


def operator_in_string():
    print("============ operator_in_string")
    s = "A linguagem Python é demais!"
    s1 = "Python"
    print(s[0])  # "A"
    print(s[2:11])  # "linguagem"
    print(s[::-1])  # ""!siamed é nohtyP megaugnil A"
    s2 = s + " Sensacional!!!"  # Concatenação
    print(s2)
    s3 = s1 * 3  # Concatenando o string s1 3 vezes
    print(s3)
    print("O substring '{}' está contindo em '{}' => {}".format(s1, s, s1 in s))
    print("O substring '{}' não está contindo em '{}' => {}".format(s3, s2, s3 not in s2))


def main():
    last_position_option_1()
    last_position_option_2()
    last_position_option_3()
    range_string_1()
    range_string_2()
    range_string_3()
    range_string_4()
    range_string_5()
    range_string_6()
    range_string_7()
    range_string_8()
    range_string_9()
    range_string_10()
    range_string_11()
    range_string_12()
    range_string_13()
    parts_of_string_1()
    parts_of_string_2()
    parts_of_string_3()
    operator_in_string()



main()
