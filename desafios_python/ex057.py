sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados errados, Informe seu sexo novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
