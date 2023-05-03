casa = float(input('Valor da casa: '))
sal = float(input('Salário atual: '))
temp = float(input('Deseja pagar em quantos anos? '))
prestacao = sal / (temp / 12)
if prestacao > (sal * 30) / 100:
    print('Seu Emprestimo foi \033[1;31mRECUSADO\033[m')
elif prestacao < (sal * 30) / 100:
    print('Seu Emprestimo foi \033[1;32mACEITO\033[m')
print('Sua prestação ficou R${}'.format(prestacao))
