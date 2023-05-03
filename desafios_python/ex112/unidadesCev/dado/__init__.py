def leiaDinheiro(msg):
    valido = False
    din = 0
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[1;31mERRO: "{entrada}" é um valor inválido!\033[m')
        else:
            din = float(entrada)
            valido = True
    return din


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor