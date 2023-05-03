from math import hypot
co = int(input('Qual o comprimento do Cateto Oposto: '))
ca = int(input('QUal o comprimento do cateto Adjacente: '))
# hip = (catetoOP * catetoOP) + (catetoAD * catetoAD)
# hip = (ca ** 2) + (co ** 2) / (1/2)
hi = hypot(co, ca)
print('O Hipotenusa é {:.3f}'.format(hi))
