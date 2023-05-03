from random import randint
tot = 0
print('=-'*16)
print('VAMOS JOGADOR PAR OU IMPAR')
print('=-'*16)
while True:
    usuario = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = usuario + computador
    opcao = ' '
    while opcao not in 'PpIi':
        opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('-'*33)
    print(f'Você jogou {usuario} e computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*33)
    if opcao == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            print('=-=' * 11)
            tot += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif opcao in 'I':
        if total % 2 != 0:
            print('VOCÊ VENCEU!')
            print('=-=' * 11)
            tot += 1
        else:
            print('VOCÊ PERDEU!')
            print('=-='*11)
            break
    print('Vamo jogar novamente...')
print(f'GAMER OVER. Você venceu {tot} vezes')
