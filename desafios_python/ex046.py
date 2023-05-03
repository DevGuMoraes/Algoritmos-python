from time import sleep
from emoji import emojize
from random import choice
f = emojize(':fireworks:')
print('2022')
sleep(1)
cores = ['\033[m', '\033[36m', '\033[35m', '\033[34m',
         '\033[33m', '\033[32m', '\033[31m']
print('CONTAGEM REGRESSIVA PARA O ANO NOVO!!')
for c in range(10, -1, -1):
    print('{} {}\033[m!'.format(choice(cores), c))
    sleep(1)
print('{} BUUM BUM POOOW {}'.format(f, f))
print('\033[1;31mFELIZ ANO NOVO!!\033[m')
print('Chegamos em 2023!!')
