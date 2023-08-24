"""
    Nas linhas de códigos ao lado do marcador de linhas a bolinha vermelha é chamada de
    breakpoint que é onde falamos até onde o debugger deve
    parar antes do break point

    Step over(f10) ele executa a proxima linha de código
"""

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')