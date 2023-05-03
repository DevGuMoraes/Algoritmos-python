# deixando em formato monetário
from ex108 import moeda
p = (float(input('Digite o preço: R$')))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com {10}% de aumento ficou {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Com {50}% de desconto fico {moeda.moeda(moeda.diminuir(p, 50))}')
