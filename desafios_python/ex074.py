from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print(lista)
print(f'O maior numero da lista é {max(lista)}')
print(f'E o menor numero da lista é {min(lista)}')
