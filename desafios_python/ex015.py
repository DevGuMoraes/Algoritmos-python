dias = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))
valorkm = 0.15 * km
aluguel = 60 * dias
print('O valor total a pagar por km e dias alugados é de R${}'.format(valorkm + aluguel))
