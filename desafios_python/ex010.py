from time import sleep
din = float(input('Saldo atual da carteira: '))
print('''[ 1 ] Real
[ 2 ] Dolar
[ 3 ] Euro''')
opcao = int(input('Escolha uma opção: '))
print('''[ 1 ] Real
[ 2 ] Dolar 
[ 3 ] Euro ''')
cnv = int(input('Deseja converter por qual moeda: '))
print('Convertendo valores...')
sleep(3)
if opcao == 1:
    if opcao == 1 and cnv == 2:
        print('Em Dolar: $ {:.2f}'.format(din / 5.44))
    elif opcao == 1 and cnv == 3:
        print('Em Euro: € {:.2f}'.format(din / 6.16))
    elif opcao == 1 and cnv == 1:
        print('Nào é possivel converter para mesma moeda!')
elif opcao == 2:
    if opcao == 2 and cnv == 1:
        print('Em Real: R$ {:.2f}'.format(din * 5.44))
    elif opcao == 2 and cnv == 3:
        print('Em Euro: € {:.2f}'.format(din / 1.14))
    elif opcao == 2 and cnv == 2:
        print('Não é possivel converter para mesma moeda!')
elif opcao == 3:
    if opcao == 3 and cnv == 1:
        print('Em Real: R$ {:.2f}'.format(din * 6.16))
    elif opcao == 3 and cnv == 2:
        print('Em Dolar: $ {:.2f}'.format(din * 1.14))
    elif opcao == 3 and cnv == 3:
        print('Nào é possivel converter para mesma moeda!')
else:
    print('VALOR INVALIDO TENTE NOVAMENTE!!')