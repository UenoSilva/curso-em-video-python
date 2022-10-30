from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemviedo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadrastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADRASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(2)

