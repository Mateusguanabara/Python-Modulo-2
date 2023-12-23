from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura' )
computador = randint(0,2)
print('''Suas Opções:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador= int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ!!!')
sleep(1)
print('-=-'*8)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=-'*8)
if computador == 0:#COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE!')
    elif jogador == 2:
        print('Computador VENCE!')
    else:
        print('Jogada Inválida!')
if computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCE!')
    else:
        print('Jogada Inválida!')
if computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')
