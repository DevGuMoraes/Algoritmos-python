num = [[], []]
valor = 0
for n in range(0, 7):
    valor = int(input(f'Digite o {n}os valor : '))
    if valor % 2 == 0:
        num[0].append(valor)
    if valor % 2 != 0:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os numeros pares foram {num[0]}')
print(f'Os valores impares foram {num[1]}')

