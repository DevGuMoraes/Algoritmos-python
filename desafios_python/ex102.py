def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: O numero a ser calculado
    :param show:(Opcional) Mostra ou naoa conta.
    :return: O valor fatorial do numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
