

def sum():
    print(3 + 2)


def subtraction():
    print(7 - 5)


def multiplication():
    print(2 * 3)
    print(3 * 3.5)
    print(4 * 5.0)


def division():
    print( 9 / 3)
    print( 10 / 3)
    print( 9 / 3.0)


def division_calculating_the_coefficient():
    print(5 // 2)
    print(5 // 2)
    print(4 // 1.2)


def division_calculating_the_rest():
    print( 5 % 2 )
    print( 9 % 2.5 )


def potentiation_exponentiation():
    print( 3 ** 2 )
    print(2 ** 10)


def potentiation_radiation():
    print(9 ** (1/2))
    print(16 ** 0.5)
    print(27 ** (1/3))


def perimeter():
    base = 7
    altura = 8
    area = base * altura
    perimetro = 2 * (base + altura)
    print(area)


def circumference():
    raio = 2
    area = 3.14159 * raio ** 2
    comprimento = 2 * 3.14159 * raio
    print(f"Para o raio {raio}, a área = {area} e o comprimento = {comprimento}")


def baskara():
    a = 1
    b = -5
    c = 6
    delta = b ** 2 - 4 * a * c
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    # interpolação. forma de printar string
    print(f"Delta = {delta}, x1 = {x1} e x2 = {x2}")

def calc_of_area_circule_sector():
    # Para um círculo de raio 15, calcular a área de uma fatia com angulo = 45 graus (um pizza)
    # Isso equivale a calcular a área de uma das 8 fatias de uma pizza com 30 cm de diâmetro
    a = 45
    r = 15
    s = (a * 3.14159 * r ** 2) / 360
    print(f"Num círculo de raio {r}cm, o setor circular de ângulo {a} terá área = {s} cm^2.")



def main_methos_of_data_types():
    sum()
    subtraction()
    multiplication()
    division()
    division_calculating_the_coefficient()
    division_calculating_the_rest()
    potentiation_exponentiation()
    potentiation_radiation()
    perimeter()
    circumference()
    baskara()
    calc_of_area_circule_sector()