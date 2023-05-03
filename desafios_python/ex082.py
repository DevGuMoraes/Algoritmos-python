numeros = list()
impares = list()
pares = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r == 'N':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
numeros.sort()
pares.sort()
impares.sort()
print(f'Os numeros digitados foram {numeros}')
print(f'Os pares valores pares foram {pares}.')
print(f'E os impares foram {impares}')
