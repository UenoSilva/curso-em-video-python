def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: (valor opcional) indicando se deve ou não adicionar a situação
    :return:retorna um dicionário com várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['min'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIN'
    return r


# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
