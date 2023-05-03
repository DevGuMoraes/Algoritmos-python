l1 = int(input('Primeira linha:'))
l2 = int(input('Segunda linha: '))
l3 = int(input('Terceiro lado: '))
if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('É possivel criar um Triângulo. ')
else:
    print('É impossivel criar um triângulo. ')