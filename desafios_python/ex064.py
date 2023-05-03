n = tot = soma = 0
n = int(input('Digite um numero: [999] para parar: '))
while n != 999:
    tot += 1
    soma += n
    n = int(input('Digite um numero: [999] para parar: '))
print('Voce digitou {} valores, a soma entre os valores ficou {}'.format(tot, soma))
