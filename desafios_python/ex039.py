from datetime import date
nasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
if idade == 18:
    print('Você completou {} anos e está na hora de se ALISTAR!!')
elif idade < 18:
    print('Você ainda náo completou 18 anos')
    print('Você só poderá se alistar daqui {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já se passou {} anos do seu alistamento '.format(idade - 18))
