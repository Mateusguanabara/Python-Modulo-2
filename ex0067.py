while True:
    núm = int(input('Digite um valor para ver a tabuada:'))
    if núm < 0:
        break
    print('-' * 35)
    for c in range(1,11):
     print(f'{núm} x {c} = {núm * c}')
    print('-' * 35)
print('===== PROGRAMA TABUADA ENCERRADO , VOLTE SEMPRE!! =====')



