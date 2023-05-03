a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print('Maior numero: {}'.format(maior))
print('Menor numero: {}'.format(menor))
