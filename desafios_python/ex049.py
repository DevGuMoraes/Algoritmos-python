print('TABUADA')
from time import sleep
num = int(input('Valor da tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))
    sleep(1)
print('Fim')
