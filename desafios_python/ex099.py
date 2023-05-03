from time import sleep
'''def lin():
    print('-=' * 30)'''


def maior(* num):
    mai = cont = 0
    '''for i, v in enumerate(num):
           if i == 0:
               mai = v
           if v > mai:
               mai = v'''
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
        sleep(0.4)
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    else:
        print(f'Foram imformado {len(num)} valores ao todo. ')
        print(f'O maior valor é {mai}.')


maior(1, 2, 5, 7, 10)
maior(0, 9, 4)
maior(2, 4, 1, 5)
maior()
