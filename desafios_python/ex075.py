lista = (int(input('Digite o primeiro valor: ')),
         int(input('Digite o segundo valor: ')),
         int(input('Digite o terceiro valor: ')),
         int(input('Digite o ultimo valor: ')))
print(f'O numero 9 aparece {lista.count(9)} vezes na lista')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1} prosição')
else:
    print('O numero 3 não apareceu na lista.')
print('Os valores pares digitados foram: ', end=' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=' ')
    else:
        print('Não há numeros pares na tupla')