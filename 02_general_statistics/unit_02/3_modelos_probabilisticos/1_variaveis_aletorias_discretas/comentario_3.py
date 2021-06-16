'''Pessoal, para facilitar a resolução dos exercícios 4 a 6, segue rotina feita em Python. Obs.: A rotina só facilita os cálculos matemáticos.
Para utilizar a rotina você precisa entender o enunciado e executá-la entrando, após interpretação do enunciado, com as variáveis desejadas.'''

#Distribuição Poisson

import numpy as np
import pandas as pd
import math
from functools import reduce


#Funçao para cálculo da probabilidade de sucesso no número de tentativas informado

def probabilidade(num_ocorrencias, valor_medio, intervalo, numero_de_intervalos_avaliados):
    valor_medio_ajustado = valor_medio * numero_de_intervalos_avaliados
    return (((math.e**(-1*valor_medio_ajustado))*(valor_medio_ajustado**num_ocorrencias))/math.factorial(num_ocorrencias))


valor_medio = float(input("Informe o valor médio de ocorrências no intervalo avaliado: "))
intervalo = float(input("Informe o intervalo avaliado: "))
numero_de_intervalos_avaliados = float(input("Informe o número de intervalos avaliados: "))

print("\nValor médio de ocorrências no intervalo avaliado:{:,.4f}".format(valor_medio))
print("Intervalo avaliado: {:,.4f}".format(intervalo))
print("Número de intervalos avaliados: {:,.4f}".format(numero_de_intervalos_avaliados))
print("Valores possíveis de X: 0, 1, 2, ...")

num_ocorrencias_bem_sucedidas = int(input("Informe números de ocorrências para obter a probabilidade total:"))
resultado = probabilidade(num_ocorrencias_bem_sucedidas, valor_medio, intervalo, numero_de_intervalos_avaliados)
print("Probabilidade do número de ocorrências informado é: {:,.4f} ou {:,.2f}%".format(resultado,(resultado*100)))