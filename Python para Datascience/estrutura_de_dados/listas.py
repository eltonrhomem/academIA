notas_turmas = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0 ,6.0]
nomes= []
notas_juntas = []

for i in range(len(notas_turmas)):
    if i % 4 == 0:
        nomes.append(notas_turmas[i])
    else:
        notas_juntas.append(notas_turmas[i])

print(nomes)
print(notas_juntas)

notas = []

for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i + 1], notas_juntas[i + 2] ])
print(notas)

