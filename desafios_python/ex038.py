n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O valor maior é {} e o menor é {}.'.format(n1, n2))
elif n2 > n1:
    print('O valor maior é {} e o menor é {}.'.format(n2, n1))
else:
    print('Não existe valor maior, os valores {} e {} são iguais.'.format(n1, n2))
