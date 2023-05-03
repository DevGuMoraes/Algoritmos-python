sal = float(input('Saário atual do funcionario: '))
if sal > 1250:
    novosal = sal + (sal * 10 / 100)
else:
    novosal = sal + (sal * 15 / 100)
print('O seu novo salário será de R${:.2f}'.format(novosal))