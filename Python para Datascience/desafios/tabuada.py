"""
2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
 Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

 Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
"""

def geraTabuada(numero):
    if 1 <= numero <= 10 : 
        for multiplicador in range(0, 11):
            print(f'{numero} X {multiplicador} = {numero * multiplicador}')
    else:
        print('O número deve ser entre 1 e 10')

tabuada = int(input('Infome um número inteiro oara gerar tabuada: '))
geraTabuada(tabuada)