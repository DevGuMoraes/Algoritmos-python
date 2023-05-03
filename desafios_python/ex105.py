def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param num:uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se  deve ou não acionar a situação
    :return: dicionário com várias informações sobre a sitação da  turma.
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'    
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(3, 10, 3, 8.2, sit=True)
print(resp)
help(notas)
