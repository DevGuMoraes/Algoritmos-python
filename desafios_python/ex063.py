from time import sleep
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
termos = int(input('Quantos termos serao contados? '))
count = 0
t1 = 0
t2 = 1
t3 = 0
print('-'*30)
print('{} -> {}'.format(t1, t2), end='')
while count <= termos:
    t3 = t2 + t1
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
    sleep(0.8)
print(' -> Finalizado')
print('-'*30)
