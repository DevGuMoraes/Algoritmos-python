
cont = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
        'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
        'QUINZE', 'DESESEIS', 'DEZESETE', 'DEZOITO',
        'DEZENOVO', 'VINTE')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    while 0 > n or n > 20:
        n = int(input('Tente Novemnte. Digite outro numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'O numero que você digitou foi {cont[n]}')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
