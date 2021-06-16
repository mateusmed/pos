'''Para facilitar pra galera, é só importar da biblioteca scipy.stats a ferramenta binom. Ex: from scipy.stats import binom'''

#Joga uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
prob = binom.pmf(3, 5, 0.5)

#Probilidade de passar por 4 sinais de trânsito
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)

#COncurso com 12 questões, qual a probabilidade de acertar 7 questões, sendo que cada questão possui 4 alternativas
binom.pmf(7, 12, 0.25)