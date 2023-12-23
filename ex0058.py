from random import randint
computador = randint(0,10)
print('Vamo jogar , eu sou uma maquína é pensei em um n° de 0 a 10.')
print('Você quer tentar adivinhar ?')
acertou = False
papites = 0
while not acertou:
    jogador = int(input('Digite seu palpite ?'))
    papites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez?')
        elif jogador > computador:
            print('Menos...Tente mais uma vez?')
print('Você Acertou com {} Tentativas .\033[32;1m Parabéns!!!\033[m'.format(papites))



