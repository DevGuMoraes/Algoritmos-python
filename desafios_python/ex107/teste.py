from ex108 import moeda
p = (float(input('Digite o preço: R$')))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Com {10}% de aumento ficou {moeda.aumento(p, 10)}')
print(f'Com {50}% de desconto fico {moeda.diminuir(p, 50)}')
