numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Adicionando... Numeros adicionado com sucesso.')
    else:
        print('Valor duplicado... Tente um valor valido')
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar ?[S/N]')).strip().upper()[0]
    if r == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')