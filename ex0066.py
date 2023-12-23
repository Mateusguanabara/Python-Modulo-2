n = cont = soma = 0
while True:
    n = int(input('Digite um número:[999 para Parar]'))
    if n == 999:
     break
    soma += n
    cont += 1
print(f'a Soma entre eles é {soma} é os números digitados foi {cont}')
