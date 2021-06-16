import numpy as np
import statistics
import math
import matplotlib.pyplot as plt

'''postado pelos alunos no forum'''


dados = np.array("18 19 21 21 21 22 22 22 23 23 24 27".split(' '),
                 dtype=np.float64)

dados

"""
Calcula o quartil de um conjunto de dados.

K = posicao do quartil
dados = numpy.ndarray
ordernar_lista = valor boleano indicando se é para ordenar a lista ou não.
Se o valor for true a lista será ordenada

"""

def calcula_quartil(K:int,dados: np.array, orderna_lista=True):

    if(orderna_lista):
        dados = np.sort(dados)

        quartil = None
        L = (K/100)* dados.size

        if(L.is_integer()):
            posicao_numero = dados[int(L) -1]
            sucessor = dados[int(L)]
            quartil = (posicao_numero + sucessor) / 2
        else:
            posicao_numero = math.ceil(L)
            quartil = dados[posicao_numero -1]

        return quartil


q1 = calcula_quartil(25, dados) # primeiro quartil = 21
mediana = calcula_quartil(50, dados) # segundo quartil = 22
q3 = calcula_quartil(75, dados) # terceiro quartil = 23

s_q1 = "{0:.0f}".format(q1)
s_mediana = "{0:.0f}".format(mediana)
s_q3 = "{0:.0f}".format(q3)

plt.figure(figsize=(6, 6))
plt.boxplot(dados)
plt.title('Boxplot Idades')
plt.ylabel('Idade')
plt.text(1, q1, s_q1)
plt.text(1, mediana, s_mediana)
plt.text(1, q3, s_q3)
plt.show()
plt.close()