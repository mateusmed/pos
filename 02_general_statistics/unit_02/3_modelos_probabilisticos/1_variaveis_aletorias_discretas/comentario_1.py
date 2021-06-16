#Distribuição Binomial

import numpy as np
import pandas as pd
import math
from functools import reduce


'''postado no forum por um aluno'''


#Funçao para cálculo da media

def media(num_tentativas_experimento_aleatorio, probabilidade_tentativa_bem_sucedida):

return num_tentativas_experimento_aleatorio*probabilidade_tentativa_bem_sucedida


#Funçao para cálculo da variância

def variancia(num_tentativas_experimento_aleatorio, probabilidade_tentativa_bem_sucedida, probabilidade_tentativa_mal_sucedida):

return num_tentativas_experimento_aleatorio*probabilidade_tentativa_bem_sucedida*probabilidade_tentativa_mal_sucedida


#Funçao para cálculo do desvio

def desvio(num_tentativas_experimento_aleatorio, probabilidade_tentativa_bem_sucedida, probabilidade_tentativa_mal_sucedida):

return (num_tentativas_experimento_aleatorio*probabilidade_tentativa_bem_sucedida*probabilidade_tentativa_mal_sucedida)**0.5


x = int(input("Informe o número de tentativas do experimento aleatório: "))
p = float(input("Informe a probabilidade de que uma tentativa seja bem sucedida (no critério esperado - entre 0 e 1): "))
q = 1 - p
indice = list(range(0,x+1))

print("Número de tentativas do experimento aleatório: ", x)
print("Probabilidade de que uma tentativa seja bem sucedida: {:,.4f}".format(p))
print("Probabilidade de que uma tentativa seja mal sucedida: {:,.4f}".format(q))
print("Valores possíveis de X: ", indice)


#Funçao para cálculo da probabilidade de sucesso no número de tentativas informado

def probabilidade(num_tentativas_avaliada):

combinacao = math.factorial(x)/(math.factorial(num_tentativas_avaliada)*math.factorial(x-num_tentativas_avaliada))
return combinacao * (p**num_tentativas_avaliada) * ((1 - p)**(x-num_tentativas_avaliada))


lista_tentativas = []
print("Informe números de tentativas bem sucedidas para obter a probabilidade total\n(digite número maior que o máximo de tentativas possíveis para parar)")
num_tentativas_bem_sucedidas = int(input("Digite um número de tentativas bem sucedidas para obter a probabilidade: "))
while (num_tentativas_bem_sucedidas<=x):
lista_tentativas.append(num_tentativas_bem_sucedidas)
num_tentativas_bem_sucedidas = int(input("Digite um número de tentativas bem sucedidas para obter a probabilidade: "))

print("\nTentativas bem sucedidas para o cálculo da probabilidade total\n===============")
print(lista_tentativas)

probabilidades = list(map(probabilidade, indice))

tabela_probabilidades = pd.Series(probabilidades, indice)

media_calculada = media(x,p)
variancia_calculada = variancia(x,p,q)
desvio_calculado = desvio(x,p,q)

print("\nO resultado médio do experimento é: {:,.4f}".format(media_calculada))
print("A variância do experimento é: {:,.4f}".format(variancia_calculada))
print("O desvio médio do experimento é: {:,.4f}".format(desvio_calculado))

print("\nProbabilidade das tentativas bem sucedidas informadas para o cálculo da probabilidade total\n===============")

probabilidade_total = 0

for item in lista_tentativas:
print("A probabilidade de {} tentativas bem sucedidas é: {:,.4f} ou {:,.2f}%".format(item, tabela_probabilidades.get(item), 100*tabela_probabilidades.get(item)))
probabilidade_total += tabela_probabilidades.get(item)

print("\nProbabilidade total: {:,.4f} ou {:,.2f}%".format(probabilidade_total,probabilidade_total*100))