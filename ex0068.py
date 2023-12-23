from random import randint
print('='*60)
print('Vamos jogar? Sou uma maquína é pensei em um número de 0 á 10:')
print('='*60)
print('Tente a Sorte!')
print('='*60)
v = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR [P/I]')).upper().strip()
    print(f'Você jogou {jogador}! é a computador jogou {computador}! é o total foi de {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você Venceu!!')
        else:
            print('Você Perdeu!!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER , você venceu {v} vezes')





