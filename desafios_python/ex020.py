from random import shuffle
a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quarto nome: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('Os alunos  sorteados foram {}'.format(lista))
