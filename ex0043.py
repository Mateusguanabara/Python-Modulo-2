peso = (float(input('Digite o Seu Peso ??')))
altura = (float(input('Digite a Sua Altura ??')))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[31m ABAIXO DO PESO \033[m , Seu IMC está -> {:.2f}'.format(imc))
elif 18.5 < imc <= 25:
    print('\033[32m PESO IDEAL \033[m , Seu IMC Está -> {:.2f} '.format(imc))
elif 25 < imc <= 30:
    print('SOBRE O PESO , Seu IMC -> {:.2f}'.format(imc))
elif 30 < imc <= 40:
    print('OBESIDADE , Você está com o IMC -> {:.2f}'.format(imc))
else:
    print('\33[31m OBESIDADE MÓRBIDA \033[m')


