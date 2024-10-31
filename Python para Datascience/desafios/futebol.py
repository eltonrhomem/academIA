"""
8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo.
 Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, 
representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, 
levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu.
 Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
"""

def determinaPonto(m, s):
    if m < s : return 0
    elif m > s : return 3
    else: return 1

def calculaPontos(marcados, sofridos):
    pontos = []
    for  index in range(len(marcados)):
        pontos.append(determinaPonto(marcados[index], sofridos[index]))
    return pontos


gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
pontos = sum(calculaPontos(gols_marcados, gols_sofridos))
print(f'A pontuação todal é {pontos}')