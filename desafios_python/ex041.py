from datetime import date
nasc = int(input('Data de nascimento do Atleta: '))
atual = date.today().year
idade = atual - nasc
print('Seu atleta tem {} anos e está na categoria: '.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 20:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
