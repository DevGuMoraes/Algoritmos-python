from time import sleep
opcao = 0
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
while opcao != 5:
    print('-'*6, 'MENU PARA CALCULO', '-'*6)
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('{} X {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior é {}'.format(maior))
        else:
            maior = n2
            print('entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite um novo numero: '))
        n2 = int(input('Digite outro numero: '))
    elif opcao > 5:
        print('Opção ínvalida, Tente outro numero.')
    print('=-='*12)
print('Finalizando Programa...')
sleep(2)
print('Volte sempre!')
