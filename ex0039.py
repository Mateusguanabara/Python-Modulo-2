from datetime import date
atual = date.today().year
nasc = int(input('Digite Sua Data De Nascimento??'))
idade = atual - nasc
print('Quem nasceu em {} Tem {} Anos em {} '.format(nasc,idade,atual))
if idade == 18:
    print('Você tem que , ALISTAR IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda Falta {} Ano Para você Alistar'.format(saldo))
    ano = atual + saldo
    print('Seu ALISTAMENTO será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter Se-ALISTADO a {}'.format(saldo))
    ano = atual - saldo
    print('Seu Alistamento foi em {} Ano'.format(ano))


