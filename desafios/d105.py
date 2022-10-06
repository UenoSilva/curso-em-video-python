def notas(* notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas de um estudante.
    :param sit: (opcional) indica a situção do aluno: Exelente, bom ou insuficiente.
    :return: retorna um dicionário com as informações do aluno.
    """
    menor = maior = soma = 0
    for k, i in enumerate(notas):
        if k == 0:
            menor = maior = i
        else:
            if i > maior:
                maior = i
            if i < menor:
                menor = i
    for g in notas:
        soma += g
    media = soma/len(notas)
    alunos = dict()
    alunos['quant'] = len(notas)
    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['media'] = media

    if sit == True:
        if media > 9.0:
            alunos['situação'] = 'Exelente'
        elif 7.0 < media < 9.0:
            alunos['situação'] = 'Bom'
        elif 5.0 < media < 7.0:
            alunos['situação'] = 'Regurla'
        else:
            alunos['situação'] = 'Insuficiente'
    return alunos


a = notas(10.0, 8.45, 9.0, 7.89, sit=True)
print(f'{a}')
