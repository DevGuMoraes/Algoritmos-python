from random import choice
n = int(input('Digite um valor de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
computador = choice(lista)
if computador == n:
    print('Parabéns você acertou!')
elif computador != n:
    print('HA HA HA, Você perdeuu!!')
else:
    print('Valor inválido. TENTE NOVAMENTE')