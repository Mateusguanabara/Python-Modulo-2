sexo = str(input('Digite Seu Sexo ? [M/F]?')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Opção Incorreta . Informe o Sexo M ou F')).upper().strip()
print('Sexo registrado {} com sucesso'.format(sexo))