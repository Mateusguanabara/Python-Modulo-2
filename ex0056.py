somaidade = 0
mediadeidade = 0
maioridadehomem = 0
homemvelho = ''
totmulher20 = 0
for c in range(1,5):
    print('-------- {}° Grupo -------'.format(c))
    nome = str(input('{}ºPessoa Com o Nome?'.format(c))).strip()
    sexo = str(input('Informe Seu Sexo?[F/[M]')).strip()
    idade = int(input('Sua Idade?'))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediadeidade = somaidade / 4
print('A Média De Idade Do Grupo é {} Anos'.format(mediadeidade))
print('O Homem Mais Velho Tem {} Anos é seu Nome é {}'.format(maioridadehomem,nome))
print('Tem No Total De {} Mulheres Com Menos De 20 Anos'.format(totmulher20))








