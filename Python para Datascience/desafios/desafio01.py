# Vamos praticar o que aprendemos até aqui solucionando os problemas propostos em código.

# Aquecimento
# 1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

# 2. Escreva um código para importar a biblioteca numpy com o alias np.

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

from random import choice, randrange
from math import pow

numbers = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numeroEscolhido = choice(numbers)
print(numeroEscolhido)

print('Vou sortear um numero de 0 a 100')
numero0a100 = randrange(0, 100)
print(numero0a100)

base = int(input('Informe a base '))
potencia = int(input('Informe a potencia '))
print(pow(base, potencia))