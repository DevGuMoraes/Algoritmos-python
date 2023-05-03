lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? (S/N)')).strip().upper()[0]
    if r == 'N':
        break
print(f'A lista tem {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrecente é {lista}')
if 5 in lista:
    print(f'O valor 5 apareceu {lista.count(5)} vezez e foi digitado nas posições', end=' ')
    for i, v in enumerate(lista):
        if v == 5:
            print(f'{i}...', end='')
    print()
else:
    print('O numero 5 não foi digitado! ')
