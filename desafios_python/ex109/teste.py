from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Com {10}% de aumento ficou {moeda.aumentar(p, 10, True)}')
print(f'Com {50}% de desconto fico {moeda.diminuir(p, 50, True)}')
