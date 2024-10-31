"""
6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
"""


def avaliaEstudante(lista):
    ordenado = sorted(lista)
    maior = ordenado[-1]
    menor = ordenado[0]
    media = sum(lista) / len(lista)
    situacao =  'APROVADO' if media > 60  else 'REPROVADO'
    print(f'O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}')

notas = [80, 70, 90, 85]
avaliaEstudante(notas)