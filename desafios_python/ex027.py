n = str(input('Informe seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Segundo nome: {}'.format(nome[len(nome) - 1]))