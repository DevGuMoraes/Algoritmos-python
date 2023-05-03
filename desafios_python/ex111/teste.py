# deixando em formato monetário
from ex111.unidadesCev import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 25)

