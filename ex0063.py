print('-'*25)
print('Sequência do Fibonacci !')
print('-'*25)
n = int(input('Quantos termos você deseja digitar?'))
t1 = 0
t2 = 1
print('~'*50)
print('{} -> {} '.format(t1,t2),end= '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3),end= '')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')


