def multiplosDe3(lista):
    mult_3 = []
    for n in lista:
        if n % 3 == 0:
            mult_3.append(n)
    return mult_3




lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
mult_3 = multiplosDe3(lista)
print(mult_3)