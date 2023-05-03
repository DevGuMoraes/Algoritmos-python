num = int(input('Informe o numero que deseja converter: '))
resp = int(input('1 para binario, 2 para octal, 3 para hexadecimal :'))
if resp == 1:
    print('{}'.format(bin(num)))
elif resp == 2:
    print('{}'.format(oct(num)))
elif resp == 3:
    print('{}'.format(hex(num)))
