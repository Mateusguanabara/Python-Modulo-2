mulher = maior = continuar = cont = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA!')
    print('-'*20)
    idade = int(input('Idade:'))
    sexo = str(input('[F/M]:')).upper().strip()
    print('-'*20)
    continuar = str(input('Quer continuar?[S/N]')).upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        cont += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continuar == 'N':
     break
print('==== VOCÊ ENCERROU O PROGRAMA! ====')
print(f'Ao todo tem {maior} pessoas acima de 18 anos')
print(f'Ao todo tem cadastrado {cont} Homens!')
print(f'Ao todo temos {mulher} Mulheres Cadastradas menos de 20 anos.')

