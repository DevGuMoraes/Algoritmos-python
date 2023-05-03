l1 = int(input('Primeira linha:'))
l2 = int(input('Segunda linha: '))
l3 = int(input('Terceiro lado: '))
if l1 < l2 + l3 or l2 < l3 + l1 or l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILATERO!')
    if l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Não é possivel criar um triândulo')