from random import randint
from time import sleep


def sorteia(num):
    print(f'Sorteando 5 valores de lista: ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        num.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def sompar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'Somando todos os valores pares de {num}, temos {soma}')


numeros = list()
sorteia(numeros)
sompar(numeros)
