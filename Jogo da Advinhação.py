import random
import time


def menu():
    print('\n------------- Bem Vindo -------------\n')
    print('Regras do nível do jogo\n')
    print('nível 1 (fácil) : acerte em menos de 10 jogadas\n')
    print('nível 2 (médio) : acerte em menos de 5 jogadas\n')
    print('nível 3 (difícil) : acerte em menos de 3 jogadas\n')
    print('\n-------------------------------------------\n')
    print('Menu de opções:\n')
    print('F - Fácil')
    print('M - Médio')
    print('D - Difícil')
    print('S - Sair do jogo')
    op = input('Digite a opção de sua escolha: ')
    return op


def escolha(tenta, name):
    i = 0
    resposta = 0
    numero = random.randint(1, 50)
    tempo = time.time()
    while resposta != numero:
        if i == tenta:
            print('Lamento, mas você atingiu o número máximo de tentativas\n')
            break
        resposta = int(input('Digite o número a ser encontrado: '))
        if resposta == numero:
            print('\nParabéns!!! Você conseguiu acertar o número sorteado.\n')
            print('Nome: {}'.format(name))
            print('Tempo de: {:.1f} segundos\n'.format((time.time() - tempo)))
            break
        elif numero > resposta:
            print('\nVocê errou para baixo... tente um número maior\n')
        elif numero < resposta:
            print('Você errou para cima... tente um número menor.')
        i = i + 1


igual = True
while igual:
    nome = input('Primeiramente, digite o seu nome: ')
    resp = menu()
    if resp == 'F' or resp == 'M' or resp == 'D' or resp == 'S':
        if resp == 'F':
            tentativas = 10
            escolha(tentativas, nome)
        elif resp == 'M':
            tentativas = 5
            escolha(tentativas, nome)
        elif resp == 'D':
            tentativas = 3
            escolha(tentativas, nome)
        elif resp == 'S':
            igual = False
    else:
        print('Alternativa errada, tente novamente!!!')
