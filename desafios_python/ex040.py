n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('\033[4;031mREPROVADO\033[m')
elif m >= 5.0 and m < 6.9:
    print('\033[4;033mRECUPERAÇÃO\033[m')
elif m >= 7.0:
    print('\033[4;032mAPROVADO\033[m')
print('Suas notas foram {} e {} e sua média é {}'.format(n1, n2, m))
