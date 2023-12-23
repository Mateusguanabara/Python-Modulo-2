n1 = float(input('Digite Sua Nota 1º Bimestre?'))
n2 = float(input('Digite Sua Nota 2 º Bimestre?'))
média = (n1 + n2) / 2
if média < 5.0 :
    print('\033[2;31mREPROVADO!!\033[m , \nSua nota Total = {:.2f}'.format(média))
elif média < 6.9:
    print('\033[2;31mRECUPERAÇÃO!!!!\033[m')
else:
    print('\033[1;32mAPROVADO!!!\033[m')