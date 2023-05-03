from datetime import date
totmaior = 0
totmenor = 0
atual = date.today().year
for c in range(0, 7):
    nasc = int(input('Ano de Nascimento: '))
    idade = atual - nasc
    print('{} anos'.format(idade))
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} pessoas alcançaram a maior idade'.format(totmaior))
print('{} pessoas ainda não alcançaram a maior idade.'.format(totmenor))
