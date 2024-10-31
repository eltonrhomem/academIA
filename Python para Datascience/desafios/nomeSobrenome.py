"""
7. Você recebeu uma demanda para tratar 2 
listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. 
As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
"""

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

for n in range(0, len(nomes)):
    nome = nomes[n].capitalize()
    sobrenome = sobrenomes[n].capitalize()
    print(f'Nome completo: {nome} {sobrenome} ')