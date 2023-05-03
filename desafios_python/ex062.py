print('=-='*12)
print('Gerador de PA')
print('=-='*12)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 1
opcao = 3
termo = primeiro
while opcao != 0:
    print('{}'.format(termo), end='')
    print(end=' -> ' if n != 10 else '\n')
    termo += razao
    n += 1
    if n > 10:
        print('------ ESCOLHA UM TERMO ------')
        print('''[ 0 ] Para finalizar programa
[ 1 ] Para novo termo''')
        opcao = int(input('Escolha uma opcao: '))
        if opcao == 1:
            primeiro = int(input('Informe outro termo: '))
            razao = int(input('Nova razao: '))
            termo = primeiro
            n = 1
print('Encerrando...')
