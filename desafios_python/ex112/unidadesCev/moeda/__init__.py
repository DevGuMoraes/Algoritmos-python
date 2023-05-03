def aumentar(preco=0, taxa=0, formato=False):
    '''
    :param preco:preço informado pelo usuario
    :param taxa:porcentagem que será aumentada do valor desejado
    :param formato:retorna o valor monetario sem precisar chamar moeda()
    :return: retorna o preço mais a taxa  do valor e o preço princ formatado
    '''
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    '''
    :param preco:preço informado pelo usúario
    :param taxa:porcentagem que será diminuida do valor principal
    :param formato:retorna o valor monetario sem precisar chamar moeda()
    :return:retorna o preço menos a taxa do valor princ e o preço já formatado
    '''
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    '''
    :param preco:valor principal informado pelo usuario
    :param formato:retorna o valor monetario sem precisar chamar moeda()
    :return:retorna a metade do preço ou preço dividido em dois
    '''
    res = preco / 2
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    '''
    :param preco:valor principal inforamdo pelo usuario
    :param formato:retorna o valor monetario sem preicasar chamar moeda()
    :return: retorna o dobro do preço princ
    '''
    res = preco * 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    '''
    :param preco:valor principal informado pelo usuario
    :param moeda:mostra a moeda deseja pelo usuario
    :return:retorna valor formatado já com a moeda R$
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(p=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True):}')
    print(f'{taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(p, taxar, True)}')
    print('-' * 30)

