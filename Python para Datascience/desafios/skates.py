"""
5. Você foi contratado(a) como cientista de dados de uma associação de skate. 
Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. 
Retorne a média para apresentar o texto:

"Nota da manobra: [media]"
"""

notas = []
for n in range(0, 4):
    nota = float(input(f'Informe a nota {n + 1}: '))
    notas.append(nota)

soma = sum(notas)
media = soma/5
print(f'A nota do skatista é {media}')