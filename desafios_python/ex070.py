print('-'*30)
print('{:^29}'.format('SUPER BARATÃO'))
print('-'*30)
tot = totmil = menor = barato = count = 0
while True:
    count += 1
    prod = str(input('Nome do Produto: '))
    preco = float(input('preço: R$'))
    tot += preco
    if preco >= 1000:
        totmil += 1
    if count == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O Total da compra foi:{tot}')
print(f'Temos {totmil} produtos mais caros que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}')
