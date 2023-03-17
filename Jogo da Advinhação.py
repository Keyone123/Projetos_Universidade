import random
import time


def menu():
    resp = 0
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
    resp = input('Digite a opção de sua escolha: ')
    return resp


repetir = 1
tentativas = 0
i = 0
resposta = 0
while repetir == 1:
    nome = input('Por favor, jogador, digite o seu nome: ')
    r = menu()
    if r == 'F':
        tentativas = 10
        num = random.randint(1, 100)
        tempo = time.time()
        while resposta != num:
            if i == 10:
                print('Lamento, mas você atingiu o número máximo de tentativas\n')
                break
            resposta = int(input('Por favor, digite o número a ser encontrado: '))
            if resposta == num:
                print('\nParabéns!!! Você conseguiu acertar o número sorteado.\n')
                print('Nome: {}'.format(nome))
                print('Tempo de: {:.1f} segundos\n'.format((time.time() - tempo)))
                break
            elif num > resposta:
                print('\nVocê errou para baixo... tente um número maior\n')
            elif num < resposta:
                print('\nVocê errou para cima... tente um número menor.\n')
            i = i + 1
    elif r == 'M':
        tentativas = 5
        num = random.randint(1, 100)
        tempo = time.time()
        while resposta != num:
            if i == 5:
                print('Lamento, mas você atingiu o número máximo de tentativas\n')
                break
            resposta = int(input('Por favor, digite o número a ser encontrado: '))
            if resposta == num:
                print('\nParabéns!!! Você conseguiu acertar o número sorteado.\n')
                print('Nome: {}'.format(nome))
                print('Tempo de: {:.1f} segundos\n'.format((time.time() - tempo)))
                break
            elif num > resposta:
                print('\nVocê errou para baixo... tente um número maior\n')
            elif num < resposta:
                print('Você errou para cima... tente um número menor.')
            i = i + 1
    elif r == 'D':
        tentativas = 3
        num = random.randint(1, 100)
        tempo = time.time()
        while resposta != num:
            if i == 3:
                print('Lamento, mas você atingiu o número máximo de tentativas\n')
                break
            resposta = int(input('Por favor, digite o número a ser encontrado: '))
            if resposta == num:
                print('\nParabéns!!! Você conseguiu acertar o número sorteado.\n')
                print('Nome: {}'.format(nome))
                print('Tempo de: {:.1f} segundos\n'.format((time.time() - tempo)))
                break
            elif num > resposta:
                print('\nVocê errou para baixo... tente um número maior\n')
            elif num < resposta:
                print('Você errou para cima... tente um número menor.')
            i = i + 1
    elif r != 'F' and r != 'M' and r != 'D':
        print('\nOpção incorreta, por favor, digite uma opção dentro do esperado\n')
    print('Você deseja repetir a operação?')
    print('1-Continuar 2-Sair')
    repetir = int(input())
