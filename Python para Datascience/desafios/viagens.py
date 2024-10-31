"""
9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. 
O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), 
a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
"""
# import decimal 
# from decimal import Decimal

def gastosComHotel(quantidadeDeDias):
    precoDiaria = 150.00
    return precoDiaria * quantidadeDeDias

def gastosComGasolina(kmPorLitro, precoGasolina, kmPercorrido):
    return round( (kmPercorrido/kmPorLitro) * precoGasolina, 2 )

def gastosComPasseioEAlimentacao(cidade, qtdDias):
    gastos = {
        'Salvador': 200,
        'Fortaleza': 400,
        'Natal': 250,
        'Aracaju': 300
    }

    gastoDaCidade = gastos[cidade]
    return round(gastoDaCidade * qtdDias, 2)

print('uma viagem de 3 dias para Salvador partindo de Recife')
print(f'Gasto com Hotel:  R$ {gastosComHotel(3)}')
print(f'Gasto com gasolina: R$ {gastosComGasolina(14, 5, 200 * 2)}')
print(f'Gasto com alimentação: R$ {gastosComPasseioEAlimentacao('Salvador', 3)}')


