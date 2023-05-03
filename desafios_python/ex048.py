print('Calculo de impares e multiplos de três.')
s = 0
tot = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        tot = tot + 1
        s += c
print('A soma entre todos os {} valores impares e multiplos de 3 é {}'.format(tot, s))
