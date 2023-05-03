print('=-='*12)
print('Gerador de PA')
print('=-='*12)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = 1
termo = primeiro
while n <= 10:
    print('{}'.format(termo), end='')
    print(end=' -> ' if n != 10 else '')
    termo += razao
    n += 1
