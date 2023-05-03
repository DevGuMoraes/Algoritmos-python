tot = soma = media = maior = menor = 0
r = 'Ss'
while r not in 'Nn':
    n = int(input('Digite um numero: '))
    tot += 1
    soma += n
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r != 'S':
        r = 'Nn'
media = soma / tot
print('A você digitou {} numeros e a media entre todos os valores foi: {}'.format(tot, media))
print('O maior valor é {} e o menor é {}'.format(maior, menor))
print('E a soma é {}'.format(soma))
