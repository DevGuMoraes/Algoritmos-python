from time import sleep
c = ['\033[m',          # 0 - COR ZERO
     '\033[0;30;41m',    # 1 - VERMELHO
     '\033[0;30;42m',    # 2 - VERDE
     '\033[0;30;43m',    # 3 - AMARELO
     '\033[0;30;44m',    # 4 - AZUL
     '\033[0;30;45m',    # 5 - ROXO
     '\033[7;97m'        # 6 - BRANCO
     ]


def ajuda(com):
    titulo(f'Acessando o manual de comando \'{comando}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=1):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sleep(1)
titulo('ATE LOGO', 1)
