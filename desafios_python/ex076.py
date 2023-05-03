listagem = ('Lápis', 1.75,
            'Borracha', 0.50,
            'Air Fryer', 257.99,
            'TV', 1009.99,
            'Caneta', 2.99,
            'Celular', 3500.00,
            'Notbook', 3500.00,
            'Relógio', 500.50,
            'Torradeira', 100.00)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>9.2f}')